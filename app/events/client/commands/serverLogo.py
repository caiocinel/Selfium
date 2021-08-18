import discord
from discord.ext import commands
from app.vars.client import client
from app.helpers import Notify

@commands.guild_only()
@client.command(aliases=['servericon','guildicon','guildlogo'])
async def serverLogo(ctx):
    notify = Notify(ctx=ctx, title='Server Icon')
    notify.prepair()
    notify.image(title=f"🖼️ Here's {ctx.guild.name} logo", image=f"{ctx.guild.icon_url.BASE + ctx.guild.icon_url._url}")


