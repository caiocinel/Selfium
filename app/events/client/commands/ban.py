import discord
import asyncio
from discord.ext import commands
from app.vars.client import client
from app.helpers import notify, delete

@client.command()
@commands.guild_only()
@commands.has_permissions(ban_members=True)
async def ban(ctx, Member: commands.Greedy[discord.Member]=None):
    await ctx.message.delete()
    try:
        for t in range(len(Member)):
            if not Member[t] or Member[t].id == client.user.id: await notify.error(ctx,'No users were informed');return            
            await asyncio.sleep(0.3)
            await ctx.guild.ban(Member[t])
            await notify.success(ctx, f'You have successfully banned the user {Member[t].display_name}!', 8)
    except Exception as e:
        await notify.exception(ctx, e)

