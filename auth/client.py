import cli
import auth
import vars
from config import cfg

def client():
    if(auth.token(cfg['token'])):
        auth.loop.create_task(vars.client.start(cfg['token'], bot=False))
    else:
        cli.tokenError('client')
        exit()