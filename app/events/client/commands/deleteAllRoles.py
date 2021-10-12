import asyncio
from discord.ext import commands
from app.vars.client import client
from app.helpers import Notify
from app.filesystem import ignore, error


@client.command(aliases=['removeAllRoles'])
@commands.guild_only()
@commands.has_permissions(manage_channels=True)
async def deleteAllRoles(ctx):
    notify = Notify(ctx=ctx, title ='Deleting All Channels...')
    notify.prepair()

    if str(ctx.guild.id) in ignore.getIgnore():
        notify.error(content='The server {} is being ignored'.format(ctx.guild.name))
        return

    for role in ctx.guild.roles:
        try:
            await role.delete()
            await asyncio.sleep(0.33)
        except Exception as e:
            error(e)
            pass         
    else:
        notify.success(content=f'Successful deleted all roles')    