const { spawn } = require('child_process');
const fs = require('fs');

const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const port = 9222;

const chrome = spawn(chromePath, [
  '--headless=new',
  '--disable-gpu',
  `--remote-debugging-port=${port}`,
  '--no-first-run',
  '--no-default-browser-check',
  'about:blank'
]);

async function run() {
  await new Promise(r => setTimeout(r, 1500));
  
  // Get websocket debugger URL
  const res = await fetch(`http://127.0.0.1:${port}/json/version`);
  const data = await res.json();
  const wsUrl = data.webSocketDebuggerUrl;
  console.log('Connected to CDP:', wsUrl);

  const ws = new WebSocket(wsUrl);

  let id = 1;
  const callbacks = new Map();

  function send(method, params = {}) {
    return new Promise((resolve) => {
      const msgId = id++;
      callbacks.set(msgId, resolve);
      ws.send(JSON.stringify({ id: msgId, method, params }));
    });
  }

  ws.onmessage = (event) => {
    const msg = JSON.parse(event.data);
    if (msg.id && callbacks.has(msg.id)) {
      const cb = callbacks.get(msg.id);
      callbacks.delete(msg.id);
      cb(msg.result);
    }
  };

  await new Promise((r) => (ws.onopen = r));

  // Create new target / page
  const { targetId } = await send('Target.createTarget', { url: 'about:blank' });
  const pageWsUrl = `ws://127.0.0.1:${port}/devtools/page/${targetId}`;
  const pageWs = new WebSocket(pageWsUrl);

  let pageId = 1;
  const pageCallbacks = new Map();
  function sendPage(method, params = {}) {
    return new Promise((resolve) => {
      const msgId = pageId++;
      pageCallbacks.set(msgId, resolve);
      pageWs.send(JSON.stringify({ id: msgId, method, params }));
    });
  }

  pageWs.onmessage = (event) => {
    const msg = JSON.parse(event.data);
    if (msg.id && pageCallbacks.has(msg.id)) {
      const cb = pageCallbacks.get(msg.id);
      pageCallbacks.delete(msg.id);
      cb(msg.result);
    }
  };

  await new Promise((r) => (pageWs.onopen = r));

  // Enable Page & Emulation
  await sendPage('Page.enable');
  
  // Set real iPhone 14 device metrics (390 x 844, scale factor 2, mobile = true)
  await sendPage('Emulation.setDeviceMetricsOverride', {
    width: 390,
    height: 844,
    deviceScaleFactor: 2,
    mobile: true,
    screenOrientation: { angle: 0, type: 'portraitPrimary' }
  });

  // Navigate to viewport test
  await sendPage('Page.navigate', { url: 'file:///E:/GoogleAntigravity/Gmap-store/viewport_test.html' });
  await new Promise(r => setTimeout(r, 1000));

  // Evaluate innerWidth
  const evalRes = await sendPage('Runtime.evaluate', {
    expression: 'document.getElementById("res").innerText'
  });
  console.log('Evaluated inside page:', evalRes.result.value);

  // Capture screenshot
  const shot = await sendPage('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('test_iphone.png', Buffer.from(shot.data, 'base64'));
  console.log('Saved test_iphone.png, size:', fs.statSync('test_iphone.png').size);

  chrome.kill();
  process.exit(0);
}

run().catch(err => {
  console.error(err);
  chrome.kill();
  process.exit(1);
});
