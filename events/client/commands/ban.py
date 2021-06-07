import discord
import asyncio
from vars.client import client
from helpers import notify

@client.command()
async def ban(ctx):
    try:
        if not ctx.message.mentions:
            await notify.error(ctx, "No user found", 5)
            return
        else:
            target = ctx.message.mentions

        if ctx.message.author.guild_permissions.ban_members:

            for t in range(len(target)):
                await asyncio.sleep(0.3)
                await ctx.guild.ban(target[t])
                await notify.success(ctx, f'You have successfully banned the user {target[t].display_name}!', 8)

        else:
            await notify.error(ctx, 'You are not allowed to ban here :( ', 5)

    except Exception as e:
        await notify.exception(ctx, e)

