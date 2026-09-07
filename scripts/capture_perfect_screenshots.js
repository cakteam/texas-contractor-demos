const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');
const http = require('http');

// 1. Start lightweight local HTTP server
const PORT = 8788;
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

server.listen(PORT, () => {
  console.log(`Local web server active at http://127.0.0.1:${PORT}`);
});

// 2. Launch Chrome with CDP
const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const cdpPort = 9223;

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
  const wsUrl = data.webSocketDebuggerUrl;

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

  const targets = [
    {
      id: '01_good_roots',
      url: `http://127.0.0.1:${PORT}/03_DEMOS/01_good_roots_roofing/index.html`
    },
    {
      id: '02_a_matt',
      url: `http://127.0.0.1:${PORT}/03_DEMOS/02_a_matt_tree_service/index.html`
    },
    {
      id: '03_dapco',
      url: `http://127.0.0.1:${PORT}/03_DEMOS/03_dapco_garage_door/index.html`
    }
  ];

  const outDir = path.join(baseDir, '04_PREVIEWS');
  if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });

  for (const t of targets) {
    console.log(`\n=== Processing ${t.id} ===`);

    // Create target
    const { targetId } = await send('Target.createTarget', { url: 'about:blank' });
    const pageWsUrl = `ws://127.0.0.1:${cdpPort}/devtools/page/${targetId}`;
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
    await sendPage('Page.enable');
    await sendPage('DOM.enable');

    // --- 1. MOBILE SCREENSHOT (390 x 844, 2x scale, touch enabled) ---
    console.log(`Setting mobile device emulation (390x844 iPhone 14)...`);
    await sendPage('Emulation.setDeviceMetricsOverride', {
      width: 390,
      height: 844,
      deviceScaleFactor: 2,
      mobile: true,
      screenOrientation: { angle: 0, type: 'portraitPrimary' }
    });
    await sendPage('Emulation.setUserAgentOverride', {
      userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'
    });

    await sendPage('Page.navigate', { url: t.url });
    await new Promise(r => setTimeout(r, 2000)); // wait for Tailwind & Lucide icons

    // Verify dimensions in page
    const dims = await sendPage('Runtime.evaluate', {
      expression: `JSON.stringify({
        innerWidth: window.innerWidth,
        scrollWidth: document.documentElement.scrollWidth,
        clientWidth: document.documentElement.clientWidth
      })`
    });
    console.log(`  -> Mobile Dimensions:`, dims.result.value);

    const mobileShot = await sendPage('Page.captureScreenshot', {
      format: 'png',
      captureBeyondViewport: false
    });
    const mobilePath = path.join(outDir, `${t.id}_mobile.png`);
    fs.writeFileSync(mobilePath, Buffer.from(mobileShot.data, 'base64'));
    console.log(`  -> Saved ${mobilePath} (${fs.statSync(mobilePath).size} bytes)`);

    // --- 2. DESKTOP SCREENSHOT (1440 x 900) ---
    console.log(`Setting desktop emulation (1440x900)...`);
    await sendPage('Emulation.setDeviceMetricsOverride', {
      width: 1440,
      height: 900,
      deviceScaleFactor: 1,
      mobile: false
    });
    await sendPage('Emulation.setUserAgentOverride', {
      userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    });

    await sendPage('Page.navigate', { url: t.url });
    await new Promise(r => setTimeout(r, 1500));

    const desktopShot = await sendPage('Page.captureScreenshot', {
      format: 'png',
      captureBeyondViewport: false
    });
    const desktopPath = path.join(outDir, `${t.id}_desktop.png`);
    fs.writeFileSync(desktopPath, Buffer.from(desktopShot.data, 'base64'));
    console.log(`  -> Saved ${desktopPath} (${fs.statSync(desktopPath).size} bytes)`);

    await send('Target.closeTarget', { targetId });
    pageWs.close();
  }

  console.log('\nAll perfect screenshots generated successfully!');
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
