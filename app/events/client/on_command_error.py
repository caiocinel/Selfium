from app.vars.client import client
from app.helpers import notify, delete

@client.event
async def on_command_error(ctx, error):
    try:
        await ctx.message.delete()
        await notify.error(ctx, error)
    except:
        pass

