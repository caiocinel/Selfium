import asyncio
from discord.utils import get
from discord.ext import commands
from app.vars.client import client
from app.helpers import notify, delete, params
from app.filesystem import cfg


@client.command()
@commands.guild_only()
@commands.has_permissions(manage_channels=True)
async def createChannel(ctx, *, args = ''):
    await ctx.message.delete()
    args = params.split(args)
    if len(args) > 1:
        try:
            channelType = str.lower(args[0])
            if len(args) == 2:
                args.append(None)
            if(channelType == 'text'):
                await ctx.guild.create_text_channel(args[1],category=get(ctx.guild.categories, name=args[2]))
            elif(channelType == 'voice'):
                await ctx.guild.create_voice_channel(args[1],category=get(ctx.guild.categories, name=args[2]))
            elif(channelType == 'category'):
                await ctx.guild.create_category(args[1])
            else:
                await notify.error(ctx, f'The type of channel you provide ({args[1]}) is not supported\n ')
                return
        finally:
            await notify.success(ctx, f'The {args[0]} channel \'{args[1]}\' was created successfully')
    else:
        await notify.error(ctx, f'This command requires two parameters:\n {cfg["prefix"]}createChannel type;;name;;*category')


@client.command(aliases=['create_voice_channel'])
@commands.guild_only()
@commands.has_permissions(manage_channels=True)
async def createVoiceChannel(ctx, *, name):
    await createChannel(ctx, args='voice;;'+ name)

@client.command(aliases=['create_text_channel'])
@commands.guild_only()
@commands.has_permissions(manage_channels=True)
async def createTextChannel(ctx, *, name):
    await createChannel(ctx, args='text;;'+ name)

@client.command(aliases=['create_category','create_category_channel','createcategorychannel'])
@commands.guild_only()
@commands.has_permissions(manage_channels=True)
async def createCategory(ctx, *, name):
    await createChannel(ctx, args='category;;'+ name)
