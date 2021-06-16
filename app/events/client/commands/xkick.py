import discord
import asyncio
from app.vars.client import client
from app.helpers import notify, getUser
from discord.ext import commands

@commands.guild_only()
@client.command(aliases=['kickid','kick_id','id_kick'])
async def xkick(ctx, arg=None):
    try:
        if not arg:
            await notify.error('User ID not provided')
            return

        target = await getUser.byID(arg)
        if ctx.message.author.guild_permissions.kick_members:
                await asyncio.sleep(0.3)
                await ctx.guild.kick(target)
                await notify.success(ctx, f'You have successfully kicked the user {target.display_name}!', 8)

        else:
            await notify.error(ctx, 'You are not allowed to kick here :( ', 5)

    except Exception as e:
        await notify.exception(ctx, e)

