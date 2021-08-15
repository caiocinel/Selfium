from app.vars.client import client
from app.filesystem import cfg, save
from app.helpers import notify, delete
    
@client.command(aliases=['messageLogging'])
async def logMessages(ctx):
    await ctx.message.delete()
    cfg['msgLogger'] = not cfg['msgLogger']
    save(cfg)
    await notify.success(ctx, f"Message Logger has been set to { cfg['msgLogger'] }")
