import CONFIG_HANDLER, sys
import DATA as datas
import API
from zipfile import ZipFile
import requests
import os
import tempfile
from pathlib import Path

#CONSTANTS
HOME = os.path.expanduser("~")
BASE_PATH = "%s/.local/share/thetechrobopackagemanager" % HOME

"""
credits
https://code.tutsplus.com/tutorials/how-to-download-files-in-python--cms-30099
https://www.kite.com/python/answers/how-to-read-a-dictionary-from-a-file-in--python
https://stackoverflow.com/a/7689085/9654083
https://stackoverflow.com/a/3451150/9654083
https://stackoverflow.com/a/34603829/9654083
https://stackoverflow.com/a/273227/9654083
"""

APILoad = API.APILoad

try:
    cmd = sys.argv[1]
except Exception: 
    cmd = None
try:
    with open("%s/initialised" % BASE_PATH,"r") as file:
        pass
except Exception:
    print("TheTechRobo's packaged manager doesn't seem to be initialised. Initialise now? (Y/n)")
    init = input().lower()
    if init[0] == "y":
        print("Initialising initialisation.")
        Path("%s/stuff"% BASE_PATH).mkdir(parents=True, exist_ok=True)
        Path("%s/tmp"% BASE_PATH).mkdir(parents=True, exist_ok=True)
        Path("%s/confs"% BASE_PATH).mkdir(parents=True, exist_ok=True)
        Path('%s/confs/conf.ini' % BASE_PATH).touch()
        Path('%s/initialised' % BASE_PATH).touch()
        print("Please add this to the end of your shell's launch script (e.g. .zshrc, .bash_profile, etc):")
        print("export PATH=$PATH:%s/*" % BASE_PATH)
        print("Then come back.")
        sys.exit(0)
    else:
        sys.exit(3)
try:
    packName = sys.argv[2]
except IndexError:
    packName = None
if sys.argv == []:
    print(datas.usage)
    sys.exit(1)
elif "-h" in sys.argv:
    print(datas.usage)
    sys.exit()
elif "--help" in sys.argv:
    print(datas.usage)
    sys.exit()
elif "-v" in sys.argv or "--version" in sys.argv: 
    print(datas.version)
elif cmd == "install": 
    apiDict = APILoad()
    try:
        pDict = apiDict[packName]
        pUrl = pDict["download"]
        pV = pDict["version"]
        pAuthor = pDict["author"]
    except KeyError:
        print("Could not find the requested package")
        sys.exit(4)
    print("Going to install package %s, by %s, version %s. URL: %s" % (packName, pAuthor, pV, pUrl))
    Yn = input("Is this OK? ").lower()
    if Yn[0] != "y":
        print("Abort.")
        sys.exit(5)
    res = requests.get(pUrl)
    if res.status_code == 200: 
        with open("%s/tmp/TEMP.zip" % BASE_PATH, "wb") as file:
            file.write(res.content)
        with ZipFile("%s/tmp/TEMP.zip" % BASE_PATH, "r") as zip_ref:
            zip_ref.extractall("%s/stuff" % BASE_PATH)
    sys.exit()
elif cmd == "remove":
    api = APILoad()
    sys.exit(127)
elif cmd == "list" or cmd == "show":
    api = APILoad()
    sys.exit(127)
elif "-v" in sys.argv or "--version" in sys.argv: 
    print(datas.version)
else: 
    print(datas.unknown)
