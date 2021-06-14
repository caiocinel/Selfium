import platform, discord
from colorama import Fore
from app.vars import client
from datetime import datetime
from app.config import cfg
Time = datetime.now()

async def welcome_message():
    print(f"{Fore.CYAN}[+] - Successful login")
    print(f"""    > {Fore.GREEN}Connected As: {Fore.BLUE}{client.user.display_name}{Fore.CYAN}.
    > {Fore.GREEN}Connected At: {Fore.BLUE}{Time.strftime("%H:%M:%S")} | {Time.strftime("%Y-%m-%d")}{Fore.CYAN}.
    > {Fore.GREEN}PyVersion: {Fore.BLUE}{platform.python_version()}{Fore.CYAN}.
    > {Fore.GREEN}DpVersion: {Fore.BLUE}{discord.__version__}{Fore.CYAN}.
    > {Fore.GREEN}Prefix: {Fore.BLUE}{cfg['prefix']}{Fore.CYAN}
    """)