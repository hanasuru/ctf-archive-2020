const puppeteer = require('puppeteer');
var myArgs = process.argv.slice(2)[0];


(async () => {
  const browser = await puppeteer.launch({args: ['--no-sandbox', '--disable-setuid-sandbox']});
  const page = await browser.newPage();
  const page2 = await browser.newPage();
  await page.goto('http://104.199.120.115/login');
  await page.type('#username', 'admin');
  await page.type('#password', 'mahasiswaabadi1337');

  await page.keyboard.press('Enter');

  await page.waitForNavigation();
  try {
    await page2.goto(Buffer.from(myArgs, 'hex').toString());
  }
  catch (e){}
  await browser.close();
})().catch();

