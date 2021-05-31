import discord
from helpers import getUser, notify, delete
from vars.client import client


@client.command()
async def serverInfo(ctx):
    try:
        embed = discord.Embed(title="Server information", colour=discord.Color.purple())
        embed.set_thumbnail(url=ctx.guild.icon_url)
        userData = await getUser.byID(ctx.guild.owner_id)
        userName = f"{userData.display_name}#{userData.discriminator}"
        fields = [
            ("ID", f"```{ctx.guild.id}```", True),
            ("Owner::", f"```{userName}```", True),
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
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
            embed.set_footer(text='Selfium (◔‿◔)')
        await ctx.send(embed=embed)
    except Exception as e:
        print (e)
        await notify.error(ctx, 'Something goes wrong, check console for logs.', None, 5)