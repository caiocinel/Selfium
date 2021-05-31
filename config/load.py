import json

def load():
    with open("config.json") as loadFile:
        cfg = json.load(loadFile)
    loadFile.close()