import os
import sys
from app.vars.client import client
from app.helpers import Notify

@client.command()
async def reload(ctx):
    notify = Notify(ctx=ctx, title='Reloading')
    try:
        notify.success(content='Selfium will reload, please wait...')
        os.execv(sys.executable, ["python"] + sys.argv)
    except Exception as e:
        print(e)
        notify.error(content='Something goes wrong, verify the console logs!')
        