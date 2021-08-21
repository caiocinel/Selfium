from app.vars.client import client
from app.helpers import Notify, params
from app.filesystem import ignore


@client.command(aliases=['ignore'])
async def ignoreServer(ctx):
    notify = Notify(ctx=ctx, title='Ignoring Server...')
    notify.prepair()
    ignoreList = ignore.getIgnore()

    if str(ctx.guild.id) in ignoreList:
        del ignoreList[str(ctx.guild.id)]
        notify.success(title='',content='The server {} has been removed from the ignore list successfully'.format(ctx.guild.name))
    else:
        ignoreList[str(ctx.guild.id)] = []
        notify.success(content='The server {} has been added in ignore list successfully'.format(ctx.guild.name))

    ignore.saveIgnore(ignoreList)

    
