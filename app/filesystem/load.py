import json

try:
    with open("data/config.json") as loadFile:
        cfg = json.load(loadFile)
    loadFile.close()
except:
    cfg = None

def reloadCfg():   
    global cfg
    with open("data/config.json") as loadFile:
        cfg = json.load(loadFile)
    loadFile.close()