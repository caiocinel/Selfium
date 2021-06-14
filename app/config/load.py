import json

with open("config.json") as loadFile:
    cfg = json.load(loadFile)
loadFile.close()