from datetime import datetime

def error(message):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    with open("./logs/error.log", "a") as errorFile:
        text = ("[" + dt_string + "] ") + message + '\n'
        errorFile.write(text)
    errorFile.close()
