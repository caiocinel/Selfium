import json

def save(cfg):
    with open("config.json", "w") as writeFile:
        writeFile.write(json.dumps(cfg))
    writeFile.close()