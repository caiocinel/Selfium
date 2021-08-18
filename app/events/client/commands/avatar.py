import discord
from discord.ext import commands
from app.vars.client import client
from app.helpers import Notify

@client.command(aliases=['profilepicture'])
async def avatar(ctx, Member: discord.Member = None):
    notify = Notify(ctx=ctx, title = 'Avatar')
    notify.prepair()
    notify.image(title=f"🖼️ Here's {Member.display_name} profile picture", image=f"{Member.avatar_url.BASE + Member.avatar_url._url}")

