import discord
import asyncio
from discord.ext import commands
from app.vars.client import client
from app.helpers import notify

@client.command()
@commands.guild_only()
@commands.has_permissions(ban_members=True)
async def ban(ctx):
    try:
        if not ctx.message.mentions:
            await notify.error(ctx, "No user found", 5)
            return
        else:
            target = ctx.message.mentions
        for t in range(len(target)):
            await asyncio.sleep(0.3)
            await ctx.guild.ban(target[t])
            await notify.success(ctx, f'You have successfully banned the user {target[t].display_name}!', 8)
    except Exception as e:
        await notify.exception(ctx, e)

