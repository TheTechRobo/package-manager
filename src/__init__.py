import CONFIG_HANDLER, sys
import DATA as datas
import API
from io import BytesIO #https://stackoverflow.com/a/5711095/9654083
from zipfile import ZipFile
import requests
import os

#CONSTANTS
BASE_PATH = "~/.local/bin/thetechrobopackagemanager"

"""
credits
https://code.tutsplus.com/tutorials/how-to-download-files-in-python--cms-30099
https://www.kite.com/python/answers/how-to-read-a-dictionary-from-a-file-in--python
https://stackoverflow.com/a/7689085/9654083
"""

APILoad = API.APILoad

try:
    with open("%s/initialised" % BASE_PATH,"r") as file:
        pass
except Exception:
    print("TheTechRobo's packaged manager doesn't seem to be initialised. Initialise now? (Y/n)")
    init = input().lower()
    if init[0] == "y":
        print("Initialising initialisation.")
        sys.exit(127)
    else:
        sys.exit(3)
packName = sys.argv[2]
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
elif sys.argv[1] == "install": 
    api = APILoad()
    try:
        pUrl = api[packName[url]]
    except KeyError:
        print("Could not find the requested package")
        sys.exit(4)
    res = requests.get(pUrl)
    if res.status_code == 200: 
        with open("%s/tmp/TEMP.zip", "wb") as file:
            file.write(res.content)
        
    sys.exit(127) #mimics the shell command not found error code
elif sys.argv[1] == "remove":
    api = APILoad()
    sys.exit(127)
elif sys.argv[1] == "list" or sys.argv[1] == "show":
    api = APILoad()
    sys.exit(127)
elif "-v" in sys.argv or "--version" in sys.argv: 
    print(datas.version)
else: 
    print(datas.unknown)
