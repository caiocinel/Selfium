import discord
import asyncio
from app.vars.client import client
from app.helpers import notify, getUser
from discord.ext import commands

@client.command(aliases=['kickid','kick_id','id_kick'])
@commands.guild_only()
@commands.has_permissions(kick_members=True)
async def xkick(ctx, id):
    try:
        target = await getUser.byID(id)
        await asyncio.sleep(0.3)
        await ctx.guild.kick(target.user)
        await notify.success(ctx, f'You have successfully kicked the user {target.user.display_name}!', 8)

    except Exception as e:
        await notify.exception(ctx, e)

