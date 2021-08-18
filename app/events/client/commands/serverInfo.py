import discord
from app.helpers import getUser, Notify
from app.vars.client import client
from discord.ext import commands


@commands.guild_only()
@client.command()
async def serverInfo(ctx):
    notify = Notify(ctx=ctx, title='Server Information')
    notify.prepair()
    userData = await getUser.byID(ctx.guild.owner_id)
    fields = [
        ("ID", f"```{ctx.guild.id}```", True),
        ("Owner::", f"```{userData.user.display_name}#{userData.user.discriminator}```", True),
        ("Owner ID:", f"```{ctx.guild.owner_id}```", True),
        ("Region:", f"```{ctx.guild.region}```", True),
        ("Created in:", f'```{ctx.guild.created_at.strftime("%d/%m/%Y")}```', True),
        ("Member Count:", f"```{int(ctx.guild.member_count)}```", True), 
        ("Text Channels:", f"```{len(ctx.guild.text_channels)}```", True),
        ("Voice Channel:", f"```{len(ctx.guild.voice_channels)}```", True),
        ("Category:", f"```{len(ctx.guild.categories)}```", True),
        ("Roles", f"```{len(ctx.guild.roles)}```", True),
        ("\u200b", "\u200b", True),
    ]
    if ctx.message.author.guild_permissions.ban_members:
        fields.append(("Ban Count:", f"```{len(await ctx.guild.bans())}```", True), )
    
    notify.fields(fields=fields)
