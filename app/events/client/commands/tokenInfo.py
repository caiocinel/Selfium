import requests
import json
import discord
from app import auth
from app.helpers import Notify
from app.vars.client import client

@client.command(aliases=['infotoken', 'searchtoken', 'getuserinfobytoken'])
async def tokenInfo(ctx, token):
    notify = Notify(ctx=ctx, title='Token Information')
    notify.prepair()
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

            if "premium_type" in userInfo:
                if str(userInfo["premium_type"]) == "0":
                    userInfo["premium_type"] = "❌" 

                if str(userInfo["premium_type"]) == "1":
                    userInfo["premium_type"] = "Nitro Classic"

                if str(userInfo["premium_type"]) == "2":
                    userInfo["premium_type"] = "Nitro Gaming"
            else:
                userInfo["premium_type"] = "❌" 


            text = f"""
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

            notify.success(content=text)
    else:
        notify.error(content='The token entered is invalid!')