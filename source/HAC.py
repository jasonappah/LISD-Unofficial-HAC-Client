import requests

class HAC:
  def __init__(self, base, path = "HomeAccess"):
    self.base = base
    self.path = path
    self.fullURL = base + path
  
  def Avaliable(self, server, hacPath, returnType = 1):
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

  def Avaliable(self, fullURL, returnType = 1):
    # This function checks if we can succcessfully connect to HAC. By default it uses the variables server, hacPath, and returnType to fill in for the parameters, but you can always pass in your own. If the returnType is set to 1 (default), it will return 1 if it was able to connect, or 0 if unable to reach the server. If the returnType is set to 0, it returns a string, true or false, along with the url it connected to.
    r = requests.get(fullURL)
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

