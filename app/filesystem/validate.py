import os
from app.filesystem import cfg
from app.filesystem import load
from app.auth import token as validateToken

def validateCfg():

    if not os.path.exists('./data/config.json'):
        os.rename('./data/config.json.template', './data/config.json')

    load.reloadCfg()

    if not cfg['token']:
        token()
    if not cfg['prefix']:
        prefix()


def prefix():
    print('Enter prefix:')
    cfg['prefix'] = input()

def token(invalid=False):
    if not (invalid):
        print('Enter account token:')
    else:
        print('The token entered is invalid, try again:')
    cfg['token'] = input()
    value = validateToken(cfg['token'])
    if (value) == False:
        token(True)
