import asyncio
from discord.ext import commands
from app.vars.client import client
from app.helpers import notify, delete

@client.command(aliases=['removeallmessages', 'DAM', 'clearChannel'])
@commands.guild_only()
@commands.has_permissions(manage_messages=True)
async def deleteAllMessages(ctx):
    await delete.byContext(ctx)
    
    async for message in ctx.message.channel.history():
        try:
            await message.delete()
            await asyncio.sleep(0.33)
        except:
            pass
    else:
        await notify.success(ctx,'All messages were deleted successfully')         
        
