import json
import requests
from app import filesystem
from app.auth import token
from app.helpers import delete, notify
from app.vars.client import client

@client.command(aliases=['settoken'])
async def changeToken(ctx, token):
    await ctx.message.delete()
    if(token(token)):
        filesystem.cfg['token'] = token
        filesystem.save(filesystem.cfg)   
        await notify.success(ctx, f"Token was successfully changed, use \"{filesystem.cfg['prefix']}reload\" to apply the changes.")
    else:
        await notify.error(ctx, 'The provided token is not valid!')