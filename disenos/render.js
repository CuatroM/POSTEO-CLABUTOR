// Convierte las placas HTML de una carpeta en JPG 1080x1350.
// Uso: node disenos/render.js disenos/salida/<id>
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const dir = path.resolve(process.argv[2]);
  const placas = fs.readdirSync(dir).filter(f => /^placa-\d+\.html$/.test(f)).sort();
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  for (const f of placas) {
    await page.goto('file://' + path.join(dir, f));
    await page.evaluate(() => document.fonts.ready);
    const out = path.join(dir, f.replace('placa-', '').replace('.html', '.jpg'));
    await page.screenshot({ path: out, type: 'jpeg', quality: 92 });
    console.log(out);
  }
  await browser.close();
})();
