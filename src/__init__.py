import CONFIG_HANDLER, sys
import DATA as datas
import API

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
    sys.exit(127) #mimics the shell command not found error code
elif sys.argv[1] == "remove":
    sys.exit(127)
elif sys.argv[1] == "list" or sys.argv[1] == "show":
    sys.exit(127)
elif "-v" in sys.argv or "--version" in sys.argv: 
    print(datas.version)
else: 
    print(datas.unknown)
