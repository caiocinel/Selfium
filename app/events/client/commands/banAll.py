from discord.ext import commands
from app.vars.client import client
from app.helpers import notify

@client.command()
@commands.guild_only()
@commands.has_permissions(ban_members=True)
async def banAll(ctx):
    for member in ctx.guild.members:
        if member.id != ctx.author.id:
            await member.ban()
    else:
        await notify.success(ctx,f'All members successfully banned')
