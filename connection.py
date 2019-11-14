import requests

server = "https://lis-hac.eschoolplus.powerschool.com/"
hacPath = "HomeAccess/"
r = ""
USER_AGENT = "Mozilla/5.0 Gecko Firefox"
introMessage = "Welcome to uHAC!"



def hacAvaliable(server = server, hacPath = hacPath, returnType = 1):
# This function checks if we can succcessfully connect to HAC. By default it uses the variables server, hacPath, and returnType to fill in for the parameters, but you can always pass in your own. If the returnType is set to 1 (default), it will return 1 if it was able to connect, or 0 if unable to reach the server. If the returnType is set to 0, it returns a string, true or false, along with the url it connected to.
    r = requests.get(server + hacPath)
    if r.text != "":
        if returnType == 0:
            return "true. url: " + r.url
        else:
            return 1
    else:
        if returnType == 0:
            return "false. url: " + r.url
        else:
            return 0

def getHTML(r):
    return requests.get(r)

print(introMessage)

if hacAvaliable() == 0:
    print("We're good to go!")
else:
    print("We have a problem. Are you connected to the internet? I can't seem to reach your server.")
    raise NameError("Can't reach server")
    # I don't know if that single quote in the middle of the string is good practice. Do I need to escape it??


