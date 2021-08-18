from app.vars.client import client
from app.auth import token
from app.filesystem import cfg, save
from app.helpers import Notify
    
@client.command(aliases=['nitroSniper'])
async def giftSniper(ctx):
    notify = Notify(ctx=ctx, title='Nitro Snipping')
    notify.prepair()
    cfg['sniperToken']['enabled'] = not cfg['sniperToken']['enabled'] 
    save(cfg)
    if not token(cfg['sniperToken']['token']) and cfg['sniperToken']['enabled']:
        notify.alert(content=f'No valid token has been provided for claim, codes will be claimed in current account and codes stored on file')
    notify.success(content=f"Snipping has been set to { cfg['sniperToken']['enabled'] }")

