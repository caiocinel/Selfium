import discord
from app.vars.client import client
from app.helpers import delete, notify, getUser

@client.command(aliases=['servericon','guildicon','guildlogo'])
async def serverLogo(ctx):
    await delete.byContext(ctx)
    embed = discord.Embed(colour=discord.Colour.green())
    embed.set_author(name=f"🖼️ Here's {ctx.guild.name} logo", url=f"{ctx.guild.icon_url.BASE + ctx.guild.icon_url._url}")
    embed.set_image(url=ctx.guild.icon_url.BASE + ctx.guild.icon_url._url)
    await ctx.send(embed=embed)


