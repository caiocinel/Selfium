import app.cli
from app.vars.client import client
from app.events.client.commands.richPresence import updatePresence

@client.event
async def on_ready():
    await app.cli.welcome_message()
    await updatePresence()