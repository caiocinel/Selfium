import discord
import asyncio
from app.vars.client import client
from app.helpers import notify, getUser
from discord.ext import commands

@client.command(aliases=['removeban','xunban','unbanid', 'unban_id', 'id_unban'])
@commands.guild_only()
@commands.has_permissions(ban_members=True)
async def unban(ctx, arg=None):
    try:
        if not arg:
            await notify.error('User ID not provided')
            return

        target = await getUser.byID(arg)
        await asyncio.sleep(0.3)
        await ctx.guild.unban(target)
        await notify.success(ctx, f'You have successfully unbanned the user {target.display_name}!', 8)

    except Exception as e:
        await notify.exception(ctx, e)

