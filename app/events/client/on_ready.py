import app.cli
from app.vars.client import client

@client.event
async def on_ready():
    await app.cli.welcome_message()