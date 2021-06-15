from app.vars.client import client
from app.auth import token
from app.filesystem import cfg, save
from app.helpers import notify, delete
    
@client.command(aliases=['nitroSniper'])
async def giftSniper(ctx):
    await delete.byContext(ctx)
    cfg['sniperToken']['enabled'] = not cfg['sniperToken']['enabled'] 
    save(cfg)
    if not token(cfg['sniperToken']['token']) and cfg['sniperToken']['enabled']:
        await notify.alert(ctx, f'No valid token has been provided for claim, codes will be stored on file')
    await notify.success(ctx, f"Snipping has been set to { cfg['sniperToken']['enabled'] }")

