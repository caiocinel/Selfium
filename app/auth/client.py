from app import cli
from app import auth
from app import vars
from app import events
from app.filesystem import cfg

def client():
    if(auth.token(cfg['token'])):
        auth.loop.create_task(vars.client.start(cfg['token']))
    else:
        cli.tokenError('client')
        exit()