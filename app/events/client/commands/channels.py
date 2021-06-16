import discord
from app.helpers import getUser, notify, delete
from app.vars.client import client
from discord.ext import commands


@commands.guild_only()
@client.command(aliases=["serverChannels"])
async def channels(ctx):
    try:
        embed = discord.Embed(title="Server Channels", colour=discord.Color.purple())
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name="Voice Channels", value="** **", inline=False)
        for channel in ctx.guild.voice_channels:
            embed.add_field(name="\u2800", value=f"```{channel.name}```")
        embed.add_field(name="Categories", value="** **", inline=False)
        for channel in ctx.guild.categories:
            embed.add_field(name="\u2800", value=f"```{channel.name}```")
        embed.add_field(name="Text Channels", value="** **", inline=False)
        for channel in ctx.guild.text_channels:
            embed.add_field(name="\u2800", value=f"```{channel.name}```")
        embed.set_footer(text="Selfium (◔‿◔)")  
        await ctx.send(embed=embed)
    except Exception as e:
        print(e)
        await notify.error(ctx, "Something goes wrong, check console for logs")
