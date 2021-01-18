def api():
    import requests
    try:
        req = requests.get("https://thetechrobo.github.io/package-manager/api")
        if req.status_code == 200: 
            text = req.text
        else:
            print("There was an error processing the request. The servers may be down. (%s)" % req.status_code)
            return
    except Exception as ename:
        print("There was an error processing the API request. The servers may be down. (%s)" % ename)
        return
    return text
