import discord
from vars.client import client
from helpers import delete, notify

@client.command()
async def avatar(ctx):

    if(ctx.message.mentions):
        target = ctx.message.mentions
    else:
        target = ctx.message.author

    await delete.byContext(ctx)
    for t in range(len(target)):
        embed = discord.Embed(colour=discord.Colour.green())
        embed.set_author(name=f"🖼️ Here's {target[t].display_name} profile picture", url=f"{target[t].avatar_url.BASE + target[t].avatar_url._url}")
        embed.set_image(url=target[t].avatar_url.BASE + target[t].avatar_url._url)
        await ctx.send(embed=embed)

