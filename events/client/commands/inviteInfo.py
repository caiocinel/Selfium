import discord
from vars.client import client
from helpers import delete, getUser, getGuild

@client.command()
async def inviteInfo(ctx, arg):
    await delete.byContext(ctx)
    linkData = await client.fetch_invite(url=arg)
    if (linkData.inviter):
        inviterData = await getUser.byID(linkData.inviter.id)
    guildData = await getGuild.byID(linkData.guild.id)

    embed = discord.Embed(title="Invite information", colour=discord.Color.purple())
    embed.set_thumbnail(url=guildData.icon_url)
    fields = [
        ("ID", f"```{guildData.id}```", True),
        ("Name::", f"```{guildData.name}```", True),
        ("Description", f"```{guildData.description}```", True),
        ("Created in:", f'```{guildData.created_at.strftime("%d/%m/%Y")}```', True),
        ("Member Count:", f"```{int(linkData.approximate_member_count)}```", True), 
        ("Roles", f"```{len(guildData.roles)}```", True),
        ("Link", f"```{linkData.url}```", True),
        ("\u200b", "\u200b", True),
    ]
    for name, value, inline in fields:
        embed.add_field(name=name, value=value, inline=inline)
        
    if(inviterData):
        embed.add_field("Inviter:", f"```{inviterData.name + '#' + inviterData.discriminator}```", True)
        embed.add_field("Inviter ID:", f"```{inviterData.id}```", True)

    embed.set_footer(text='Selfium (◔‿◔)')
    await ctx.send(embed=embed)