from discord.ext import commands
from app.vars.client import client
from app.helpers import Notify

@client.command()
@commands.guild_only()
@commands.has_permissions(kick_members=True)
async def kickAll(ctx):
    notify = Notify(ctx=ctx, title='Kicking All Members...')
    notify.prepair()
    for member in ctx.guild.members:
        if member.id != ctx.author.id:
            try:
                await member.kick() 
            except:
                pass
    else:
        await notify.success(content=f'All members successfully kicked')
