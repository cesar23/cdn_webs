import sys, os,re

def getCurrentNameDir():
    abspath = os.path.abspath(__file__)
    dirname = os.path.dirname(abspath)
    return  os.path.basename(dirname)


SERVER='https://cesar23.github.io'
SERVER_PATH_URL=SERVER+"/"+ getCurrentNameDir()

CONFIG = {
    'server': SERVER,
    'dirRoot': getCurrentNameDir(),
    'links':{
        "index":SERVER_PATH_URL+"/index.html",
        "camicv":SERVER_PATH_URL+"/camicv/index.html",
    }
}