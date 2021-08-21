import asyncio
from discord.ext import commands
from app.vars.client import client
from app.helpers import Notify
from app.filesystem import ignore

@client.command(aliases=['removeallmessages', 'DAM', 'clearChannel'])
@commands.guild_only()
@commands.has_permissions(manage_messages=True)
async def deleteAllMessages(ctx):
    notify = Notify(ctx=ctx, title = 'Deleting All Channel Messages...')
    notify.prepair()

    if str(ctx.guild.id) in ignore.getIgnore():
        notify.error(content='The server {} is being ignored'.format(ctx.guild.name))
        return

    async for message in ctx.message.channel.history():
        try:
            await message.delete()
            await asyncio.sleep(0.33)
        except:
            pass
    else:
        notify.success(content='All messages were deleted successfully')         
        
