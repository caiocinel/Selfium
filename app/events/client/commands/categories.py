import discord
from discord.ext import commands
from app.helpers import Notify
from app.vars import client

@commands.guild_only()
@client.command()
async def Categories(ctx):
    notify = Notify(ctx=ctx, title="Server Categories")
    notify.prepair()
    fields = []
    for channel in ctx.guild.categories:
        fields.append(("\u2800", f"```{channel.name}```", False))
    notify.fields(fields=fields)
