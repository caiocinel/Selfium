from app.vars.client import client
from app.filesystem import log, cfg
from app.auth import nitro

@client.event
async def on_message(message):
    await client.process_commands(message)
    if(cfg['msgLogger']):
        log.msg(message)
    if(cfg['sniperToken']['enabled']):
        if 'discord.gift/' in message.content or 'discord.com/gifts/' in message.content or 'discordapp.com/gifts/' in message.content:
            await nitro.giftProcess(message)
