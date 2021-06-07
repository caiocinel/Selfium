import json
import requests
import config
from auth import token
from helpers import delete, notify
from vars.client import client

@client.command(aliases=['settoken'])
async def changeToken(ctx, arg):
    await delete.byContext(ctx)
    if(token(arg)):
        config.cfg['token'] = arg
        config.save(config.cfg)   
        await notify.success(ctx, 'Token was successfully changed, use "!reload" to apply the changes.')
    else:
        await notify.error(ctx, 'The provided token is not valid!')