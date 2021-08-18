import discord
import asyncio
from discord.ext import commands
from app.vars.client import client
from app.helpers import Notify

@client.command()
@commands.guild_only()
#@commands.has_permissions(ban_members=True)
async def ban(ctx, Member: commands.Greedy[discord.Member] = None):
    notify = Notify(ctx=ctx,title='Banning member...')
    notify.prepair()            
    if Member is None: 
        notify.error(content='No users were informed')
        return
    try:
        for t in range(len(Member)):       
            await asyncio.sleep(0.3)
            await ctx.guild.ban(Member[t])
            notify.success(content=f'You have successfully banned the user {Member[t].display_name}!')
    except Exception as e:
        notify.exception(content=e)

