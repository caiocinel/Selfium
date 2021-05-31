import asyncio
from vars.client import client
from helpers import notify, delete

@client.command(aliases=['removeallmessages', 'DAM', 'clearChannel'])
async def deleteAllMessages(ctx):
    await delete.byContext(ctx)

    if(ctx.message.author.guild_permissions.manage_messages):
        async for message in ctx.message.channel.history():
            try:
                await message.delete()
                await asyncio.sleep(0.33)
            except:
                pass         
    else:
        notify.error("You can't do this here")      
