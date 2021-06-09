import discord
from discord.ext import commands
from config import cfg

client = commands.Bot(command_prefix=cfg["prefix"], intents = discord.Intents.all() ,self_bot=True, case_insensitive=True)