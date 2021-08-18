import discord
from discord.ext import commands
from app.helpers import Notify
from app.vars import client

@commands.guild_only()
@client.command(aliases=["text_channels"])
async def textChannels(ctx):
    notify = Notify(ctx=ctx, title='Server Text Channels...')
    fields = []
    for channel in ctx.guild.text_channels:
        fields.append(("\u2800", f"```{channel.name}```", True))
    notify.fields(fields=fields)