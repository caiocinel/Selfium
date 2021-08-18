import discord
from discord.ext import commands
from app.helpers import Notify
from app.vars import client

@commands.guild_only()
@client.command(aliases=["voice_channels"])
async def voiceChannels(ctx):
    notify = Notify(ctx=ctx, title='Server Voice Channels...')
    fields = []
    for channel in ctx.guild.voice_channels:
        fields.append(("\u2800", f"```{channel.name}```", True))
    notify.fields(fields=fields)