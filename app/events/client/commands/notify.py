from app.vars.client import client
from app.auth import token
from app.filesystem import cfg, save
from app.helpers import Notify
    
@client.command()
async def notify(ctx, type:str):
    notify = Notify(ctx=ctx, title='Notify Type')
    notify.prepair()
    if(type == 'embed'):
        cfg['notifyType'] = 'embed'
    elif(type == 'message'):
        cfg['notifyType'] = 'message'
    else:
        notify.error(title='Invalid Notify Type', content='Available:\n ```embed | message```\nMessages will be used if embeds are not possible')
        return

    save(cfg)
    notify.success(content='Notify type set to: {}'.format(type))
    
