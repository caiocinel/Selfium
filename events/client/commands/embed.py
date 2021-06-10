from vars.client import client
from helpers import delete, notify

#makeEmbed(ctx, title, author, author_iconURL, description, thumbnail, 
#>> thumbnailImageURL, fields, footer, footerText, footer_iconURL, timestamp):

@client.command(aliases=['embed'])
async def simpleEmbed(ctx, title, *args):
    await delete.byContext(ctx)
    await notify.plain(ctx, title, args)
