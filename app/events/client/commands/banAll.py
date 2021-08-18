from discord.ext import commands
from app.vars.client import client
from app.helpers import Notify

@client.command()
@commands.guild_only()
@commands.has_permissions(ban_members=True)
async def banAll(ctx):
    notify = Notify(ctx=ctx, title="Banning All Members...")
    notify.prepair()
    await ctx.guild.subscribe()
    try:
        for member in ctx.guild.members:
            if member.id != ctx.author.id:
                await member.ban()
        else:
            notify.success(content='All members successfully banned')
    except Exception as e:
        notify.exception(content=e)
