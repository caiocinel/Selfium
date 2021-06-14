from vars.client import client
from config import cfg
from helpers import notify, delete
    
@client.command(aliases=['messageLogging'])
async def logMessages(ctx):
    await delete.byContext(ctx)
    cfg['msgLogger'] = not cfg['msgLogger']
    await notify.success(ctx, f"Message Logger has been set to { cfg['msgLogger'] }")
