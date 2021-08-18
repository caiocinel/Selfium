import discord
import asyncio
from app.vars.client import client
from app.helpers import Notify
from discord.ext import commands

@client.command()
@commands.guild_only()
@commands.has_permissions(kick_members=True)
async def kick(ctx, Member: commands.Greedy[discord.Member]=None):
    notify = Notify(ctx=ctx, title='Kicking Member...')
    notify.prepair()
    try:
        for t in range(len(Member)):
            if not Member[t] or Member[t].id == client.user.id: notify.error(content='No users were informed');return            
            await asyncio.sleep(0.3)
            await ctx.guild.kick(Member[t])
            notify.success(content=f'You have successfully kicked the user {Member[t].display_name}!')
    except Exception as e:
        notify.exception(content=e)

