import discord
import asyncio
from app.vars.client import client
from app.helpers import notify, getUser
from discord.ext import commands

@client.command(aliases=['banid','ban_id','id_ban'])
@commands.guild_only()
@commands.has_permissions(ban_members=True)
async def xban(ctx, id):
    try:
        target = await getUser.byID(id)
        await asyncio.sleep(0.3)
        await ctx.guild.ban(target)
        await notify.success(ctx, f'You have successfully banned the user {target.display_name}!', 8)


    except Exception as e:
        await notify.exception(ctx, e)

