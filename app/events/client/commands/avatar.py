import discord
from discord.ext import commands
from app.vars.client import client
from app.helpers import delete, sendEmbed

@client.command(aliases=['profilepicture'])
async def avatar(ctx, Member: commands.Greedy[discord.Member]):
    await delete.byContext(ctx)
    for t in range(len(Member)):
        embed = discord.Embed(colour=discord.Colour.green())
        embed.set_author(name=f"🖼️ Here's {Member[t].display_name} profile picture", url=f"{Member[t].avatar_url.BASE + Member[t].avatar_url._url}")
        embed.set_image(url=Member[t].avatar_url.BASE + Member[t].avatar_url._url)
        await sendEmbed(ctx,embed)

