import requests
import datetime
import discord
import re
from app.auth import token
from app.filesystem import cfg, gift


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