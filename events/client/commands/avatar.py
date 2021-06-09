import discord
from vars.client import client
from helpers import delete, notify, getUser

@client.command(aliases=['profilepicture'])
async def avatar(ctx):

    if(ctx.message.mentions):
        target = ctx.message.mentions
    else:
        target = ctx.message.author

    await delete.byContext(ctx)
    try:
        for t in range(len(target)):
            memberFetch = await getUser.byMember(target[t])
            embed = discord.Embed(colour=discord.Colour.green())
            embed.set_author(name=f"🖼️ Here's {memberFetch.display_name} profile picture", url=f"{memberFetch.avatar_url.BASE + memberFetch.avatar_url._url}")
            embed.set_image(url=memberFetch.avatar_url.BASE + memberFetch.avatar_url._url)
            await ctx.send(embed=embed)
    except:
        notify.error(ctx, 'Member not found')

