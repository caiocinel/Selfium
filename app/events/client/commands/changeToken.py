import json
import requests
from app import config
from app.auth import token
from app.helpers import delete, notify
from app.vars.client import client

@client.command(aliases=['settoken'])
async def changeToken(ctx, arg):
    await delete.byContext(ctx)
    if(token(arg)):
        config.cfg['token'] = arg
        config.save(config.cfg)   
        await notify.success(ctx, 'Token was successfully changed, use \"{cfg["prefix"]}reload\" to apply the changes.')
    else:
        await notify.error(ctx, 'The provided token is not valid!')