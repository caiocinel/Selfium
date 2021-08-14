import discord
import asyncio
from discord.ext import commands
from app.vars.client import client
from app.helpers import notify
from app.helpers.notify import ConsoleLog

@client.command()
@commands.guild_only()
@commands.has_permissions(manage_nicknames=True)
async def renameAll(ctx, *, nick: str):
    for member in ctx.guild.members:
        try:
            await member.edit(
                nick=nick
            )

            ConsoleLog(
                f'[LOG]: {member.name} changed to {member.display_name}'
            )

        except Exception as e:
            ConsoleLog(
                f'[ERROR]: {e.text}'
            )
    else:
        await notify.success(ctx,
            f'All members have been successfully renamed to { nick }'
        )