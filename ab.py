exec("""\nimport asyncio\nfrom pyppeteer import launch\nurl = 'https://codehs.com/sandbox/id/python-3-rTNbZc'\n\nasync def main():\n    print('huh')\n    for x in range(3000):\n        browser = await launch(options={'args': ['--no-sandbox'], 'devtools':True, 'headless':True})\n        page = await browser.newPage()\n        await page.setViewport({ 'width': 800, 'height': 600 })\n        await page.goto(url)\n        await asyncio.sleep(2)\n        await page.mouse.click(580,125,{'button': 'left'})\n        await asyncio.sleep(15)\n        await page.mouse.click(625,125,{'button': 'left'})\n        await asyncio.sleep(5)\n        # await page.screenshot({'path': 'stop.png'})\n        await asyncio.sleep(15)\n        await page.mouse.click(580,125,{'button': 'left'})\n        await asyncio.sleep(1)\n        print('huh2')\n        for y in range(35):\n            await page.mouse.click(580,400,{'button': 'left'})\n            await page.keyboard.press('KeyS')\n            await asyncio.sleep(10)\n            # await page.screenshot({'path': './test.png'})\n            await page.keyboard.press('KeyS')\n            await asyncio.sleep(10)\n            await page.keyboard.press('KeyS')\n            await asyncio.sleep(10)\n        await asyncio.sleep(1)\n        await page.mouse.click(630,125,{'button': 'left'})\n        await asyncio.sleep(5)\n        await browser.close()\nasyncio.get_event_loop().run_until_complete(main())\n""")