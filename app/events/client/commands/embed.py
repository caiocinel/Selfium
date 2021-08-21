from discord import Colour
from app.vars.client import client
from app.helpers import Notify, params
from app.filesystem import cfg

@client.command(aliases=['embed'])
async def simpleEmbed(ctx, *, args):
    notify = Notify(ctx=ctx, title='Embed')
    args = params.split(args)
    if not len(args) > 2:
        if len(args) == 2:
            notify.success(content=args[0], title=args[1], color=Colour.default())
        else:
            notify.success(content=args[0], title='')
    else:
        notify.error(content=f'Bad Usage\nExample: {cfg["prefix"]}embed Message;;Title')
