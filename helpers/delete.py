async def byMessage(message):
    await message.delete()

async def byContext(ctx):
    async for message in ctx.message.channel.history(limit=1):
        await message.delete()