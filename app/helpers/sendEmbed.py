
async def sendEmbed(ctx,embed):
    if ctx.channel.permissions_for(ctx.author).embed_links:
        await ctx.send(embed=embed)
        return

    message = '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'
    for fields in embed.fields:
        if fields.name != '\u200b':
            message += '**' + fields.name + '**: ' + fields.value + '\n'

    message += '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'

    if embed.footer.text:
        message += '**' + embed.footer.text + '**'

    message = message.replace('`','')

    await ctx.send(message)