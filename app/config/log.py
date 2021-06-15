from datetime import datetime

def error(message):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    with open("data/error.log", "a", encoding="utf-8") as errorFile:
        text = ("[" + dt_string + "] ") + message + '\n'
        errorFile.write(text)
    errorFile.close()


def msg(message):
    now = datetime.now()
    author = message.author
    if message.guild:
        guild = message.guild.name
    else:
        guild = 'DM'
    message = message.content
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    with open("data/msg.log", "a", encoding="utf-8") as msgFile:
        if not author.name:
            text = ("[" + dt_string +' - ' + guild+"] ")+ 'Webhook - ' + message + '\n'   
        else:
            text = ("[" + dt_string +' - ' + guild+"] ")+ author.name + '#' + author.discriminator + '-' + message + '\n'
        msgFile.write(text)
    msgFile.close()

