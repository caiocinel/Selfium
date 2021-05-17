import discord
from vars.client import client
from helpers import delete, getUser
from cli import notify

@client.command(aliases=['Ban'])
async def ban(ctx, Member: discord.Member = None):
    try:
        if not Member or Member == ctx.author:
            await notify.error(ctx, "No user found", None, 5)
            return
        if ctx.message.author.guild_permissions.ban_members:
            await ctx.guild.ban(Member)
            await notify.success(ctx, f'You have successfully banned the user {Member.display_name}!', None, 8)
        else:
            await notify.error(ctx, 'You are not allowed to ban here :( ', None, 5)
    except:
        await notify.error(ctx, f'Something went wrong, try again!', None, 5)
