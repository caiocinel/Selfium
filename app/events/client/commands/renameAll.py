import discord
import asyncio
from discord.ext import commands
from app.vars.client import client
from app.helpers import notify

@client.command()
@commands.guild_only()
@commands.has_permissions(manage_nicknames=True)
async def renameAll(ctx, *, nick: str):
    for member in ctx.guild.members:
        await member.edit(nick=nick)
    else:
        await notify.success(ctx,f'All members have been successfully renamed to { nick }')
