import discord
from vars.client import client
from helpers import delete, notify

@client.command()
async def avatar(ctx, Member: discord.Member=None):
    try:
        if(Member):
            target = Member
        else:
            target = ctx.author
        await delete.byContext(ctx)
        embed = discord.Embed(colour=discord.Colour.green())
        embed.set_author(name=f"🖼️ Here's {target.display_name} profile picture", url=f"{target.avatar_url}")
        embed.set_image(url=target.avatar_url)
        await ctx.send(embed=embed)
    except:
        await notify.exception()