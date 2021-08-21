import discord
import asyncio
from discord.ext import commands
from app.vars.client import client
from app.helpers import Notify
from app.filesystem import ignore


@client.command()
@commands.guild_only()
@commands.has_permissions(manage_nicknames=True)
async def renameAll(ctx, *, nick: str):
    notify = Notify(ctx=ctx, title = 'Renaming All Members...')
    notify.prepair()

    if str(ctx.guild.id) in ignore.getIgnore():
        notify.error(content='The server {} is being ignored'.format(ctx.guild.name))
        return

    for member in ctx.guild.members:
        await member.edit(nick=nick)
    else:
        notify.success(content=f"All members have been successfully renamed to { nick }")