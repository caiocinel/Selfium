from discord.ext import commands
from app.vars.client import client
from app.helpers import delete, notify, getUser

@client.command(aliases=['setGuildName'])
@commands.guild_only()
@commands.has_permissions(manage_guild=True)
async def setServerName(ctx, *, arg):
    await ctx.guild.edit(name=arg)
    await notify.success(ctx, f'Server Name was successful set to {arg}')
    
