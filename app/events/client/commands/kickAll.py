from discord.ext import commands
from app.vars.client import client
from app.helpers import notify

@client.command()
@commands.guild_only()
@commands.has_permissions(kick_members=True)
async def kickAll(ctx):
    for member in ctx.guild.members:
        if member.id != ctx.author.id:
            await member.kick()
    else:
        await notify.success(ctx,f'All members successfully kicked')
