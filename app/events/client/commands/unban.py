import discord
import asyncio
from app.vars.client import client
from app.helpers import Notify, getUser
from discord.ext import commands

@client.command(aliases=['removeban','xunban','unbanid', 'unban_id', 'id_unban'])
@commands.guild_only()
@commands.has_permissions(ban_members=True)
async def unban(ctx, id):
    notify = Notify(ctx=ctx, title='Unbaning Member...')
    notify.prepair()
    target = await getUser.byID(id)
    await asyncio.sleep(0.3)
    await ctx.guild.unban(target.user)
    notify.success(content=f'You have successfully unbanned the user {target.user.display_name}!')

