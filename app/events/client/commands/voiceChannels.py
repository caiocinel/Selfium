import discord
from discord.ext import commands
from app.helpers import notify, delete
from app.vars import client

@commands.guild_only()
@client.command(aliases=["voice_channels"])
async def voiceChannels(ctx):
    await delete.byContext(ctx)
    try:
        embed = discord.Embed(title="Voice Channels", colour=discord.Color.purple())
        embed.set_thumbnail(url=ctx.guild.icon_url)
        for channel in ctx.guild.voice_channels:
            embed.add_field(name="\u2800", value=f"```{channel.name}```")
        embed.set_footer(text="Selfium (◔‿◔)")  
        await ctx.send(embed=embed)
    except Exception as e:
        print(e)
        await notify.error(ctx, "Something goes wrong, check console for logs")