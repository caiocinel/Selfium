import discord
from discord.ext import commands
from app.filesystem import cfg
from app.filesystem import validate

validate.validateCfg()
client = commands.Bot(command_prefix=cfg["prefix"], case_insensitive=True, self_bot=True, guild_subscription_options = discord.GuildSubscriptionOptions.off())