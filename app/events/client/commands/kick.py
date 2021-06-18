import discord
import asyncio
from app.vars.client import client
from app.helpers import notify
from discord.ext import commands

@client.command()
@commands.guild_only()
@commands.has_permissions(kick_members=True)
async def kick(ctx):
    try:
        if not ctx.message.mentions:
            await notify.error(ctx, "No user found", 5)
            return
        else:
            target = ctx.message.mentions

        for t in range(len(target)):
            await asyncio.sleep(0.3)
            await ctx.guild.kick(target[t])
            await notify.success(ctx, f'You have successfully kicked the user {target[t].display_name}!', 8)
    except Exception as e:
        await notify.exception(ctx, e)

