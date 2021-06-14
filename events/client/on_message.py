from vars.client import client
from config import log, cfg

@client.event
async def on_message(message):
    await client.process_commands(message)
    if(cfg['msgLogger']):
        log.msg(message)
