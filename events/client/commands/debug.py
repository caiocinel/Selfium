import discord
from vars.client import client
from helpers import delete, notify

@client.command()
async def debug(ctx):

    a = await client.fetch_guild(ctx.guild.id)

    print(a)