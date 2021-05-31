import json
from config import cfg

def save():
    with open("config.json", "w") as writeFile:
        writeFile.write(json.dumps(cfg))
    writeFile.close()