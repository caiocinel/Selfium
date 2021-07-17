import discord
import asyncio
from app.vars.client import client
from app.helpers import notify, delete
from discord.ext import commands

@client.command()
@commands.guild_only()
@commands.has_permissions(kick_members=True)
async def kick(ctx, Member: commands.Greedy[discord.Member]=None):
    await delete.byContext(ctx)
    try:
        for t in range(len(Member)):
            if not Member[t] or Member[t].id == client.user.id: await notify.error(ctx,'No users were informed');return            
            await asyncio.sleep(0.3)
            await ctx.guild.kick(Member[t])
            await notify.success(ctx, f'You have successfully kicked the user {Member[t].display_name}!', 8)
    except Exception as e:
        await notify.exception(ctx, e)

