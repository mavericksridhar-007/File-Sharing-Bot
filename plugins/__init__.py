#(©)Codexbotz
#@iryme

from aiohttp import web

async def handle_get(request):
    return web.Response(text="✅ Bot is alive!")

async def handle_post(request):
    data = await request.json()
    # If you're using Pyrogram's built-in webhook handling, this is optional.
    return web.Response(text="ok")

async def web_server():
    app = web.Application()
    app.router.add_get("/", handle_get)   # for UptimeRobot
    app.router.add_post("/", handle_post) # for Telegram Webhook
    return app

