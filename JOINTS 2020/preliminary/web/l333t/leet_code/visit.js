const puppeteer = require('puppeteer');
var myArgs = process.argv.slice(2)[0];


(async () => {
  const browser = await puppeteer.launch({args: ['--no-sandbox', '--disable-setuid-sandbox']});
  const page = await browser.newPage();
  await page.goto('http://ctf.joints.id:1337/login');
  await page.type('#username', 'admin');
  await page.type('#password', 'bajigurnamapasswordnya');

  await page.keyboard.press('Enter');

  await page.waitForNavigation();
  try {
    await page.goto(Buffer.from(myArgs, 'hex').toString());
  }
  catch (e){}
  await browser.close();
})().catch();

