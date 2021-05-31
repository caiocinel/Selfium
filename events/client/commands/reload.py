import os
import sys
import auth
from vars.client import client
from helpers import delete, notify

@client.command()
async def reload(ctx):
    try:
        await delete.byContext(ctx)
        await notify.success(ctx, 'Selfium will reload, please wait...', None)
        os.execv(sys.executable, ["python"] + sys.argv)
    except Exception as e:
        print(e)
        await notify.error(ctx, 'Something goes wrong, verify the console logs!', None)
        