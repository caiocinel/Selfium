import discord
import asyncio
from app.vars.client import client
from app.helpers import Notify, getUser
from discord.ext import commands

@client.command(aliases=['kickid','kick_id','id_kick'])
@commands.guild_only()
@commands.has_permissions(kick_members=True)
async def kickbyid(ctx, id):
    notify = Notify(ctx=ctx, title='Kicking Member...')
    notify.prepair()
    try:
        target = await getUser.byID(id)
        await asyncio.sleep(0.3)
        await ctx.guild.kick(target.user)
        notify.success(content=f'You have successfully kicked the user {target.user.display_name}!')

    except Exception as e:
        notify.exception(content=e)