from discord.ext import commands
from app.vars.client import client
from app.helpers import Notify

@client.command(aliases=['setGuildName'])
@commands.guild_only()
@commands.has_permissions(manage_guild=True)
async def setServerName(ctx, *, name):
    notify = Notify(ctx=ctx, title='Renaming Server...')
    await ctx.guild.edit(name=name)
    notify.success(content=f'Server Name was successful set to {name}')
    
