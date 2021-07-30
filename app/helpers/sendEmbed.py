
async def sendEmbed(ctx,embed):
    if ctx.channel.permissions_for(ctx.author).embed_links:
        message = await ctx.send(embed=embed)
        return message

    message = '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'
    for fields in embed.fields:
        if fields.name != '\u200b':
            message += '**' + fields.name + '**: ' + fields.value + '\n'

    if embed.image.url:
        message += embed.image.url + '\n'

    message += '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'

    if embed.footer.text:
        message += '**' + embed.footer.text + '**'

    message = message.replace('`','')

    message = await ctx.send(message)
    return message