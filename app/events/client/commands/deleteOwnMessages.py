import asyncio, discord
from app.vars.client import client
from app.helpers import notify, delete, sendEmbed

@client.command(aliases=['removemymessages', 'dmm', 'clearmymessage', 'dom'])
async def deleteMyMessages(ctx, amount, status=True):
    await delete.byContext(ctx)

    DeletedCount = 0
    MessageList = []

    try:
        if (ctx.guild):
            await ctx.message.channel.purge(limit=int(amount),bulk=True)
            await notify.success(ctx, "Deleted {} messages from the chat".format(amount))
        else:
            Embed = discord.Embed(description=f"> Deleted messages: **{int(DeletedCount)}** / **{len(MessageList)}**.\n> Current Status: **Starting...**", color=discord.Colour.blue())
            Message = await sendEmbed(ctx, Embed)
            async for message in ctx.message.channel.history():
                try:
                    if len(MessageList) < int(amount) and message and not message == Message and message.author == ctx.author:
                        MessageList.append(message)
                except Exception as e:
                    pass
            for message in MessageList:
                try:
                    await message.delete()
                    await asyncio.sleep(0.5)
                    DeletedCount = DeletedCount + 1

                    if (Message.embeds):
                        Embed = discord.Embed(description=f"> Deleted messages until now: **{int(DeletedCount)}** / **{len(MessageList)}**.\n> Current Status: **In progress...**", color=discord.Colour.orange())
                        await Message.edit(embed=Embed)
                    else:
                        await Message.edit(f"> Deleted messages until now: **{int(DeletedCount)}** / **{len(MessageList)}**.\n> Current Status: **In progress...**")
                except Exception as e:
                    pass

            if (Message.embeds):
                Embed = discord.Embed(description=f"> Total number deleted messages: **{int(DeletedCount)}** / **{len(MessageList)}**.\n> Current Status: **All Done!**", color=discord.Colour.green())
                await Message.edit(embed=Embed)
            else:
                await Message.edit(f"> Total number deleted messages: **{int(DeletedCount)}** / **{len(MessageList)}**.\n> Current Status: **All done!**")

            await asyncio.sleep(5);
            await Message.delete();
            
    except Exception as e:
        await notify.error(ctx, "Something goes wrong, try again!")