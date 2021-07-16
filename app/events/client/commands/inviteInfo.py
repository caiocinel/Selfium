import discord
from app.vars.client import client
from app.helpers import delete, getUser, getGuild

@client.command()
async def inviteInfo(ctx, link):
    try:
        await delete.byContext(ctx)
    except:
        pass

    linkData = await client.fetch_invite(url=link)
    if (linkData.inviter):
        inviterData = await getUser.byID(linkData.inviter.id)
    try:
        guildData = await getGuild.byID(linkData.guild.id)
    except:
        guildData = linkData.guild

    embed = discord.Embed(title="Invite information", colour=discord.Color.purple())
    embed.set_thumbnail(url=guildData.icon_url)
    fields = [
        ("ID", f"```{guildData.id}```"),
        ("Name::", f"```{guildData.name}```"),
        ("Description", f"```{guildData.description}```"),
        ("Created in:", f'```{guildData.created_at.strftime("%d/%m/%Y")}```'),
        ("Member Count:", f"```{int(linkData.approximate_member_count)}```"), 
        ("Link", f"```{linkData.url}```"),
        ("\u200b", "\u200b"),
    ]
    for name, value in fields:
        embed.add_field(name=name, value=value, inline=False)
        
    if (linkData.inviter):
        embed.add_field(name="Inviter ID:", value=f"```{inviterData.user.id}```")
        embed.add_field(name="Inviter:", value=f"```{inviterData.user.name + '#' + inviterData.user.discriminator}```")

    embed.set_footer(text='Selfium (◔‿◔)')
    await ctx.send(embed=embed)