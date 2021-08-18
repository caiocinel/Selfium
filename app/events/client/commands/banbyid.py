import discord
import asyncio
from app.vars.client import client
from app.helpers import Notify, getUser
from discord.ext import commands

@client.command(aliases=['banid','ban_id','id_ban','xban'])
@commands.guild_only()
@commands.has_permissions(ban_members=True)
async def banbyid(ctx, id):
    notify = Notify(ctx=ctx, title="Banning User By ID")
    notify.prepair()
    try:
        target = await getUser.byID(id)
        await asyncio.sleep(0.3)
        await ctx.guild.ban(target.user)
        notify.success(content=f'You have successfully banned the user {target.user.display_name}!')
    except Exception as e:
        notify.exception(content=e)

