import json

def save(cfg):
    with open("data/config.json", "w") as writeFile:
        writeFile.write(json.dumps(cfg))
    writeFile.close()