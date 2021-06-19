import asyncio
from app.vars.client import client
from app.helpers import notify, delete

@client.command(aliases=['removemymessages', 'dmm', 'clearmymessage'])
async def deleteMyMessages(ctx, amount):
    await delete.byContext(ctx)

    if(isinstance(int(float(amount)), int) and int(float(amount)) > 0):
        messagesNumber = int(float(amount))
    else:
        await notify.error(ctx, 'Enter a valid lenght')
        return
        
    if (messagesNumber > int(200)):
        await notify.error(ctx, 'The current message limit is 200')
        return

    if (messagesNumber):
        try:
            i = 0
            async for message in ctx.message.channel.history().filter(lambda m: m.author == client.user):
                if(i == messagesNumber):
                    await notify.success(ctx, f' {messagesNumber} message(s) have been deleted!')
                    return
                try:
                    await message.delete()
                    i += 1
                    await asyncio.sleep(0.33)
                except:
                    pass               
        except:
            await notify.exception(ctx)