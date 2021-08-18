import discord
from app.vars.client import client
from app.helpers import Notify, getUser, getGuild

@client.command()
async def inviteInfo(ctx, link):
    notify = Notify(ctx=ctx, title='Invite information')
    notify.prepair()
    linkData = await client.fetch_invite(url=link)
    
    if (linkData.inviter):
        inviterData = await getUser.byID(linkData.inviter.id)
    try:
        guildData = await getGuild.byID(linkData.guild.id)
    except:
        guildData = linkData.guild

    fields = [
        ("ID", f"```{guildData.id}```", False),
        ("Name::", f"```{guildData.name}```", False),
        ("Description", f"```{guildData.description}```", False),
        ("Created in:", f'```{guildData.created_at.strftime("%d/%m/%Y")}```', False),
        ("Member Count:", f"```{int(linkData.approximate_member_count)}```", False), 
        ("Link", f"```{linkData.url}```", False),
        ("\u200b", "\u200b", False),
    ]
        
    if (linkData.inviter):
        fields.append(("Inviter ID:", f"```{inviterData.user.id}```", False))
        fields.append(("Inviter:", f"```{inviterData.user.name + '#' + inviterData.user.discriminator}```", False))

    notify.fields(fields=fields)