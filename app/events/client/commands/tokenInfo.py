import requests
import json
import discord
from app import auth
from app.helpers import notify, delete
from app.vars.client import client

@client.command(aliases=['infotoken', 'searchtoken', 'getuserinfobytoken'])
async def tokenInfo(ctx, token):
    await delete.byContext(ctx)
    if(auth.token(token)):
        userInfo = auth.parse(auth.token(token))
        if (userInfo):
            if str(userInfo["phone"]) == "None":
                userInfo["phone"] = "❌"
            else:
                userInfo["phone"] = {str(userInfo["phone"])}

            if str(userInfo["verified"]) == "None":
                userInfo["verified"] = "❌"
            else:
                userInfo["verified"] = "✔️"

            if str(userInfo["mfa_enabled"]) == "False":
                userInfo["mfa_enabled"] = "❌"
            else:
                userInfo["mfa_enabled"] = "✔️"

            if str(userInfo["nsfw_allowed"]) == "False":
                userInfo["nsfw_allowed"] = "❌"
            else:
                userInfo["nsfw_allowed"] = "✔️"

            if str(userInfo["premium_type"]) == "0":
                userInfo["premium_type"] = "❌" 

            if str(userInfo["premium_type"]) == "1":
                userInfo["premium_type"] = "Nitro Classic"

            if str(userInfo["premium_type"]) == "2":
                userInfo["premium_type"] = "Nitro Gaming"

            embed = discord.Embed(colour=discord.Colour.green())
            embed.set_author(
                name=client.user.display_name,
                icon_url=f"https://cdn.discordapp.com/avatars/{client.user.id}/{client.user.avatar}.png",
            )
            embed.add_field(
                name="Token Account Info:",
                value=(
                    f"""
            Username: ```{str(userInfo['username']) + '#' + str(userInfo['discriminator'])}```
            ID: ```{str(userInfo['id'])}```
            E-mail: ```{str(userInfo['email'])}```
            Verified Mail: ```{str(userInfo['verified'])}``` 
            premium_type: ```{str(userInfo['premium_type'])}```
            Enabled NFSW: ```{str(userInfo['nsfw_allowed'])}```
            2FA: ```{str(userInfo['mfa_enabled'])}```
            Phone: ```{userInfo['phone']}```
            Token: ```{token}```
            """
                ),
                inline=True,
            )
            embed.set_thumbnail(
                url=f"""https://cdn.discordapp.com/avatars/{str(userInfo['id'])}/{str(userInfo['avatar'])}.png"""
            )
            await ctx.send(embed=embed)
    else:
        await notify.error(ctx, 'The token entered is invalid!')