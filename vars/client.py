import discord
from discord.ext import commands
from config import cfg

client = commands.Bot(command_prefix=cfg["prefix"], case_insensitive=True)