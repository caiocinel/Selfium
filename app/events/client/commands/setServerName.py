from discord.ext import commands
from app.vars.client import client
from app.helpers import delete, notify, getUser

@client.command(aliases=['setGuildName'])
@commands.guild_only()
@commands.has_permissions(manage_guild=True)
async def setServerName(ctx, *, name):
    await ctx.guild.edit(name=name)
    await notify.success(ctx, f'Server Name was successful set to {name}')
    
