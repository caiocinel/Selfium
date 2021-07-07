import discord
from app.vars.client import client
from app.helpers import notify


@client.command()
async def userInfo(ctx, Member: discord.Member = None):

    if not (Member):
        await notify.error(ctx, 'No user has passed')
        return

    try:
        if (Member.bot):
            IsBot = '✔️'
        else:
            IsBot = '❌'

        if (Member.premium_since):
            Booster = '✔️'
        else:
            Booster = '❌'
            
        embed = discord.Embed(title="User Info:", colour=Member.colour)
        embed.set_thumbnail(url=Member.avatar_url)
        embed.set_footer(text='Selfium (◔‿◔)')
        fields = [(f"User:", f'```{str(Member)}```', True),
                    ("ID:", f'```{Member.id}```', True),
                    ("Bot?", f'```{IsBot}```', True),
                    ("Status: ", f'```{str(Member.status).title()}```', True),
                    ("Activity:", f"```{str(Member.activity.type).split('.')[-1].title() if Member.activity else 'N/A'} {Member.activity.name if Member.activity else ''}```", True),
                    ("Created In:", f'```{Member.created_at.strftime("%d/%m/%Y")}```', True),
                    ("Joined In:", f'```{Member.joined_at.strftime("%d/%m/%Y")}```', True),
                    ("Booster?", f'```{Booster}```', True)]
        for name, value, inline in fields: embed.add_field(name=name, value=value, inline=inline)
        await ctx.send(embed=embed)
    except Exception as e:
        print(e)
        await notify.error(ctx, e)
