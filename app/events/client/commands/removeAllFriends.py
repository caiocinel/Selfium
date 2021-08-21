import discord
import asyncio
from app.vars.client import client
from app.helpers import Notify, getUser
from app.filesystem import log

@client.command(aliases=['rAF', 'removefriendlist'])
async def removeAllFriends(ctx):
    for friend in client.user.friends:
        try:
            await friend.remove_friend()
            print(f"[INFO]: Friend removed {friend.display_name}.")
        except Exception as e:
            print(f"[ERROR]: Error while removing {friend.display_name} from your friend list\nError: {e.text}")