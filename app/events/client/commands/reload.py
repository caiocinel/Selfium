import os
import sys
from app import auth
from app.vars.client import client
from app.helpers import delete, notify

@client.command()
async def reload(ctx):
    try:
        await ctx.message.delete()
        await notify.success(ctx, 'Selfium will reload, please wait...', None)
        os.execv(sys.executable, ["python"] + sys.argv)
    except Exception as e:
        print(e)
        await notify.error(ctx, 'Something goes wrong, verify the console logs!', None)
        