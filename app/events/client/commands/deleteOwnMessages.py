import asyncio
from app.vars.client import client
from app.helpers import notify, delete

#Delete number of messages from DiscordPy client (This function was partially done by Github Copilot)
@client.command(aliases=['removemymessages', 'dmm', 'clearmymessage'])
async def deleteMyMessages(ctx, amount):
    await delete.byContext(ctx)

    if int(amount) < 1:
        await notify.error(ctx, 'Please enter a number greater than 0')
        return

    try:
        await ctx.message.channel.purge(limit=int(amount))
        await notify.success(ctx, "Deleted {} messages from the chat".format(amount))
    except:
        await notify.error(ctx, "Something goes wrong, try again!")

    




