const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');
const http = require('http');

// 1. Local HTTP server
const PORT = 8789;
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
  console.log(`Web server running on http://127.0.0.1:${PORT}`);
});

// 2. Launch Chrome CDP
const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const cdpPort = 9224;

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
      url: `http://127.0.0.1:${PORT}/03_DEMOS/01_good_roots_roofing/index.html`,
      actions: [
        { scroll: 0, wait: 300 },
        { scroll: 180, wait: 200 },
        { scroll: 420, wait: 200 },
        { scroll: 750, wait: 200 },
        { 
          eval: `
            const mat = document.getElementById('calcMaterial');
            if (mat) { mat.value = 'class4'; }
            if (window.calculateRoofCost) calculateRoofCost();
          `, 
          wait: 400 
        },
        { scroll: 880, wait: 300 },
        { scroll: 1200, wait: 300 },
        { scroll: 500, wait: 200 },
        { scroll: 0, wait: 300 }
      ]
    },
    {
      id: '02_a_matt',
      url: `http://127.0.0.1:${PORT}/03_DEMOS/02_a_matt_tree_service/index.html`,
      actions: [
        { scroll: 0, wait: 300 },
        { scroll: 220, wait: 200 },
        { scroll: 500, wait: 200 },
        { scroll: 800, wait: 200 },
        { 
          eval: `
            if (window.openEstimatorModal) openEstimatorModal('Storm Hazard Crane Removal');
          `, 
          wait: 400 
        },
        { scroll: 800, wait: 400 },
        { 
          eval: `
            if (window.closeEstimatorModal) closeEstimatorModal();
          `, 
          wait: 200 
        },
        { scroll: 1250, wait: 300 },
        { scroll: 400, wait: 200 },
        { scroll: 0, wait: 300 }
      ]
    },
    {
      id: '03_dapco',
      url: `http://127.0.0.1:${PORT}/03_DEMOS/03_dapco_garage_door/index.html`,
      actions: [
        { scroll: 0, wait: 300 },
        { scroll: 200, wait: 200 },
        { scroll: 480, wait: 200 },
        { scroll: 760, wait: 200 },
        { 
          eval: `
            if (window.selectSymptom) {
              selectSymptom('Broken Spring (Loud Bang)', 'Do not attempt to operate manually. High tension danger.');
            }
          `, 
          wait: 400 
        },
        { scroll: 760, wait: 400 },
        { 
          eval: `
            if (window.closeDispatchModal) closeDispatchModal();
          `, 
          wait: 200 
        },
        { scroll: 1200, wait: 300 },
        { scroll: 400, wait: 200 },
        { scroll: 0, wait: 300 }
      ]
    }
  ];

  const rawFramesBase = path.join(baseDir, '04_PREVIEWS', 'visual_hooks', '_raw_frames');

  for (const t of targets) {
    console.log(`\n=== Capturing Scroll Frames for ${t.id} ===`);
    const targetDir = path.join(rawFramesBase, t.id);
    if (!fs.existsSync(targetDir)) fs.mkdirSync(targetDir, { recursive: true });

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

    // Mobile Viewport (390 x 844, 2x retina)
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
    await new Promise(r => setTimeout(r, 2000));

    let frameIndex = 0;
    for (const act of t.actions) {
      if (act.scroll !== undefined) {
        await sendPage('Runtime.evaluate', {
          expression: `window.scrollTo({ top: ${act.scroll}, behavior: 'instant' });`
        });
      }
      if (act.eval) {
        await sendPage('Runtime.evaluate', { expression: act.eval });
      }
      if (act.wait) {
        await new Promise(r => setTimeout(r, act.wait));
      }

      const shot = await sendPage('Page.captureScreenshot', {
        format: 'png',
        captureBeyondViewport: false
      });
      const frameName = `frame_${String(frameIndex++).padStart(2, '0')}.png`;
      const framePath = path.join(targetDir, frameName);
      fs.writeFileSync(framePath, Buffer.from(shot.data, 'base64'));
    }

    console.log(`  -> Saved ${frameIndex} frames to ${targetDir}`);
    await send('Target.closeTarget', { targetId });
    pageWs.close();
  }

  chrome.kill();
  server.close();
  console.log('\nAll frames captured successfully!');
  process.exit(0);
}

run().catch(err => {
  console.error(err);
  chrome.kill();
  server.close();
  process.exit(1);
});
