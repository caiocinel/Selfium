import asyncio
from discord.ext import commands
from app.vars.client import client
from app.helpers import notify, delete

@commands.guild_only()
@client.command(aliases=['removeallmessages', 'DAM', 'clearChannel'])
async def deleteAllMessages(ctx):
    await delete.byContext(ctx)

    if(ctx.message.guild) :
        if not (ctx.message.author.guild_permissions.manage_messages):
            notify.error(ctx,"You can't do this here")  
            return

    async for message in ctx.message.channel.history():
        try:
            await message.delete()
            await asyncio.sleep(0.33)
        except:
            pass         
        
