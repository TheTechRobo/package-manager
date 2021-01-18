def api():
    import requests,sys
    try:
        req = requests.get("https://thetechrobo.github.io/package-manager/api")
        if req.status_code == 200: 
            text = req.text
        else:
            print("There was an error processing the request. The servers may be down. (%s)" % req.status_code)
            sys.exit(2)
    except Exception as ename:
        print("There was an error processing the API request. The servers may be down. (%s)" % ename)
        sys.exit(2)
    return text

def parse(objInput):
    import ast
    return ast.literal_eval(objInput)

def APILoad():
    print("Loading API...")
    loaded = api()
    api = parse(loaded)
    return api

