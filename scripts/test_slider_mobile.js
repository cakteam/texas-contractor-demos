const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');
const http = require('http');

const PORT = 8791;
const baseDir = path.resolve(__dirname, '..');

const server = http.createServer((req, res) => {
  let reqPath = decodeURI(req.url.split('?')[0]);
  if (reqPath === '/') reqPath = '/index.html';
  const filePath = path.join(baseDir, reqPath);
  
  if (fs.existsSync(filePath) && fs.statSync(filePath).isFile()) {
    const ext = path.extname(filePath).toLowerCase();
    const mimeTypes = {
      '.html': 'text/html',
      '.css': 'text/css',
      '.js': 'application/javascript',
      '.png': 'image/png',
      '.jpg': 'image/jpeg',
      '.svg': 'image/svg+xml'
    };
    res.writeHead(200, { 'Content-Type': mimeTypes[ext] || 'application/octet-stream' });
    fs.createReadStream(filePath).pipe(res);
  } else {
    res.writeHead(404);
    res.end('Not found');
  }
});

server.listen(PORT, () => console.log(`Server on http://127.0.0.1:${PORT}`));

const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const cdpPort = 9225;

const chrome = spawn(chromePath, [
  '--headless=new',
  '--disable-gpu',
  `--remote-debugging-port=${cdpPort}`,
  '--no-first-run',
  '--no-default-browser-check',
  'about:blank'
]);

async function run() {
  await new Promise(r => setTimeout(r, 1500));

  const res = await fetch(`http://127.0.0.1:${cdpPort}/json/version`);
  const data = await res.json();
  const ws = new WebSocket(data.webSocketDebuggerUrl);

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

  const targets = [
    { name: 'goodroots', url: `http://127.0.0.1:${PORT}/goodroots/index.html` },
    { name: 'amatttree', url: `http://127.0.0.1:${PORT}/amatttree/index.html` },
    { name: 'dapcodoor', url: `http://127.0.0.1:${PORT}/dapcodoor/index.html` }
  ];

  for (const t of targets) {
    const { targetId } = await send('Target.createTarget', { url: 'about:blank' });
    const pageWs = new WebSocket(`ws://127.0.0.1:${cdpPort}/devtools/page/${targetId}`);
    let pId = 1;
    const pCallbacks = new Map();
    function sendPage(method, params = {}) {
      return new Promise(res => {
        const mId = pId++;
        pCallbacks.set(mId, res);
        pageWs.send(JSON.stringify({ id: mId, method, params }));
      });
    }
    pageWs.onmessage = e => {
      const m = JSON.parse(e.data);
      if (m.id && pCallbacks.has(m.id)) {
        const cb = pCallbacks.get(m.id);
        pCallbacks.delete(m.id);
        cb(m.result);
      }
    };
    await new Promise(r => (pageWs.onopen = r));
    await sendPage('Page.enable');
    await sendPage('DOM.enable');

    await sendPage('Emulation.setDeviceMetricsOverride', {
      width: 390,
      height: 844,
      deviceScaleFactor: 2,
      mobile: true,
      screenOrientation: { angle: 0, type: 'portraitPrimary' }
    });

    await sendPage('Page.navigate', { url: t.url });
    await new Promise(r => setTimeout(r, 2000));

    const metrics = await sendPage('Runtime.evaluate', {
      expression: `JSON.stringify({
        innerWidth: window.innerWidth,
        scrollWidth: document.documentElement.scrollWidth,
        clientWidth: document.documentElement.clientWidth,
        hasSlider: !!document.querySelector('.ba-slider-container')
      })`
    });

    console.log(`${t.name}:`, metrics.result.value);

    await send('Target.closeTarget', { targetId });
    pageWs.close();
  }

  chrome.kill();
  server.close();
  process.exit(0);
}

run().catch(err => {
  console.error(err);
  chrome.kill();
  server.close();
  process.exit(1);
});
