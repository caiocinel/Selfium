import discord
from discord.ext import commands
from app.vars.client import client
from app.helpers import Notify

@commands.guild_only()
@client.command(aliases=['guildbanner'])
async def serverBanner(ctx):
    notify = Notify(ctx=ctx, title='Server Banner')
    notify.prepair()
    notify.image(title=f"🖼️ Here's {ctx.guild.name} banner", image=f"{ctx.guild.banner_url.BASE + ctx.guild.banner_url._url}")


