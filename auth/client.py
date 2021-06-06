import cli
import auth
import vars
import events
from config import cfg

def client():
    if(auth.token(cfg['token'])):
        auth.loop.create_task(vars.client.start(cfg['token']))
    else:
        cli.tokenError('client')
        exit()