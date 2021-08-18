from app.vars.client import client
from app.filesystem import cfg, save
from app.helpers import Notify
    
@client.command(aliases=['messageLogging'])
async def logMessages(ctx):
    notify = Notify(ctx=ctx, title='Message Logging')
    notify.prepair()
    cfg['msgLogger'] = not cfg['msgLogger']
    save(cfg)
    notify.success(content=f"Message Logger has been set to { cfg['msgLogger'] }")
