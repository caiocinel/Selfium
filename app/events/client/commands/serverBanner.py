import discord
from discord.ext import commands
from app.vars.client import client
from app.helpers import delete, notify, getUser

@commands.guild_only()
@client.command(aliases=['guildbanner'])
async def serverBanner(ctx):
    await delete.byContext(ctx)
    embed = discord.Embed(colour=discord.Colour.green())
    embed.set_author(name=f"🖼️ Here's {ctx.guild.name} banner", url=f"{ctx.guild.banner_url.BASE + ctx.guild.banner_url._url}")
    embed.set_image(url=ctx.guild.banner_url.BASE + ctx.guild.banner_url._url)
    await ctx.send(embed=embed)


