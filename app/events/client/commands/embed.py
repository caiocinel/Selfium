from app.vars.client import client
from app.helpers import delete, notify, params
from app.filesystem import cfg

@client.command(aliases=['embed'])
async def simpleEmbed(ctx, *, args):
    await ctx.message.delete()
    args = params.split(args)
    if not len(args) > 2:
        if len(args) == 2:
            await notify.plain(ctx, args[0], args[1])
        else:
            await notify.plain(ctx, args[0])
    else:
        await notify.error(ctx, f'Bad Usage\nExample: {cfg["prefix"]}embed Message;;Title')
