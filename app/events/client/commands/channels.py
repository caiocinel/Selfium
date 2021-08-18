import discord
from app.helpers import getUser, Notify
from app.vars.client import client
from discord.ext import commands


@commands.guild_only()
@client.command(aliases=["serverChannels"])
async def channels(ctx):
    notify = Notify(ctx=ctx, title="Server Channels", color=discord.Color.purple())
    notify.prepair()
    fields = [("Voice Channels", "** **", False)]
    for channel in ctx.guild.voice_channels:
        fields.append(("\u2800", f"```{channel.name}```", True))
    fields.append(("Categories", "** **", False))
    for channel in ctx.guild.categories:
        fields.append(("\u2800", f"```{channel.name}```", True))
    fields.append(("Text Channels", "** **", False))
    for channel in ctx.guild.text_channels:
        fields.append(("\u2800", f"```{channel.name}```", True))
    notify.fields(fields=fields)


