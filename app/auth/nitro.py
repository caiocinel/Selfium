import requests
import datetime
import discord
import re
from app.auth import token
from app.filesystem import cfg, gift

''' This file is part of discord-sniper by lnxcz, licensed under the MIT license:
MIT License

Copyright (c) 2020 LnX

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

def giftProcess(message):
    data = gift.load()
    start = datetime.datetime.now()
    if "discord.gift/" in message.content:
        code = re.findall("discord[.]gift/(\w+)", message.content)
    if "discordapp.com/gifts/" in message.content:
        code = re.findall("discordapp[.]com/gifts/(\w+)", message.content)
    if 'discord.com/gifts/' in message.content:
        code = re.findall("discord[.]com/gifts/(\w+)", message.content)
    for code in code:
        if len(code) == 16 or len(code) == 24:
            if not token(cfg['sniperToken']['token']):
                headers = {'Authorization': cfg['token']}
            else:
                headers = {'Authorization': cfg['sniperToken']['token']}

            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
                headers=headers,
            ).text
            elapsed = datetime.datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'
            if 'This gift has been redeemed already.' in r:
                print(""
                    f"\n{Fore.RED}{time} - Nitro is Already Redeemed" + Fore.RESET)
                NitroInfo(elapsed, code)
            elif 'subscription_plan' in r:
                print(""
                    f"\n{Fore.GREEN}{time} - Nitro Successfuly Claimed!" + Fore.RESET)
                NitroInfo(elapsed, code)
                if notification:
                    toaster.show_toast("Sniper",
                                    "Nitro Claimed! Look into console",
                                    icon_path="./drop.ico",
                                    duration=7)
                if webhooknotification:
                    data = {
                        "embeds": [{
                            "title": "Successfully Sniped Nitro Gift!",
                            "description": f"Congratulations, good job! You can view your Nitro Gifts in your inventory.\n\nNitro Gift Server:\n{message.guild}\n\nNitro Gift Sender:\n{message.author}\n\nNitro Gift Code:\n{code}",
                            "url": "https://github.com/lnxcz/discord-sniper",
                            "color": 16732345,
                            "footer": {
                            "text": "lnxcz's sniper"
                            },
                            "image": {
                            "url": "https://i.imgur.com/9QVtF0t.png"
                            }
                            }],
                            "username": "Nitro",
                            "avatar_url": "https://i.imgur.com/44N46up.gif"
                            }
                    requests.post(webhook, json=data)
            elif 'Unknown Gift Code' in r:
                print(""
                    f"\n{Fore.YELLOW}{time} - Unknown Nitro Gift Code" + Fore.RESET)
                NitroInfo(elapsed, code)