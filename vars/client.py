import discord, platform, colorama, datetime
from discord.ext import commands
from config import cfg
from colorama import Fore
from datetime import datetime
Time = datetime.now()
client = commands.Bot(command_prefix=cfg["prefix"], intents = discord.Intents.all() ,self_bot=True)

@client.event
async def on_ready():
    print(f"{Fore.CYAN}[+] - Successful login")
    print(f"""    > {Fore.GREEN}Connected As: {Fore.BLUE}{client.user.display_name}{Fore.CYAN}.
    > {Fore.GREEN}Connected At: {Fore.BLUE}{Time.strftime("%H:%M:%S")} | {Time.strftime("%Y-%m-%d")}{Fore.CYAN}.
    > {Fore.GREEN}PyVersion: {Fore.BLUE}{platform.python_version()}{Fore.CYAN}.
    > {Fore.GREEN}DpVersion: {Fore.BLUE}{discord.__version__}{Fore.CYAN}.
    """)