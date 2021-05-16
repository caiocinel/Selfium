def getMemberAvatarURL(ctx):
    mention = ctx.message.mentions[0]
    return f'''https://cdn.discordapp.com/avatars/{mention.id}/{mention.avatar}.png?size=2048'''