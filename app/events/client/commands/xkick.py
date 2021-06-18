import discord
import asyncio
from app.vars.client import client
from app.helpers import notify, getUser
from discord.ext import commands

@client.command(aliases=['kickid','kick_id','id_kick'])
@commands.guild_only()
@commands.has_permissions(kick_members=True)
async def xkick(ctx, arg=None):
    try:
        if not arg:
            await notify.error('User ID not provided')
            return

        target = await getUser.byID(arg)
        await asyncio.sleep(0.3)
        await ctx.guild.kick(target)
        await notify.success(ctx, f'You have successfully kicked the user {target.display_name}!', 8)

    except Exception as e:
        await notify.exception(ctx, e)

