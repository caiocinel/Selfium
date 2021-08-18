import json
import requests
from app import filesystem
from app.auth import token
from app.helpers import Notify
from app.vars.client import client

@client.command(aliases=['settoken'])
async def changeToken(ctx, token):
    notify = Notify(ctx=ctx, title="Changing Token")
    notify.prepair()
    if(token(token)):
        filesystem.cfg['token'] = token
        filesystem.save(filesystem.cfg)   
        notify.success(content=f"Token was successfully changed, use \"{filesystem.cfg['prefix']}reload\" to apply the changes.")
    else:
        notify.error(content='The provided token is not valid!')