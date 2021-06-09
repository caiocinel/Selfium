import discord
from vars.client import client
from helpers import delete, getUser, getGuild

@client.command()
async def inviteInfo(ctx, arg):
    
    try:
        await delete.byContext(ctx)
    except:
        pass

    linkData = await client.fetch_invite(url=arg)
    if (linkData.inviter):
        inviterData = await getUser.byID(linkData.inviter.id)
    try:
        guildData = await getGuild.byID(linkData.guild.id)
    except:
        guildData = linkData.guild

    embed = discord.Embed(title="Invite information", colour=discord.Color.purple())
    embed.set_thumbnail(url=guildData.icon_url)
    fields = [
        ("ID", f"```{guildData.id}```", True),
        ("Name::", f"```{guildData.name}```", True),
        ("Description", f"```{guildData.description}```", True),
        ("Created in:", f'```{guildData.created_at.strftime("%d/%m/%Y")}```', True),
        ("Member Count:", f"```{int(linkData.approximate_member_count)}```", True), 
        ("Link", f"```{linkData.url}```", True),
        ("\u200b", "\u200b", True),
    ]
    for name, value, inline in fields:
        embed.add_field(name=name, value=value, inline=inline)
        
    if (linkData.inviter):
        embed.add_field(name="Inviter ID:", value=f"```{inviterData.id}```", inline=True)
        embed.add_field(name="Inviter:", value=f"```{inviterData.name + '#' + inviterData.discriminator}```", inline=True)

    embed.set_footer(text='Selfium (◔‿◔)')
    await ctx.send(embed=embed)