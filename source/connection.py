# Maybe these useful links will help jog your mind and let you figure out what it is you were doing last night.

# r = requests.post("https://httpbin.org/post", data=main.formdata)
# https://3.python-requests.org/user/quickstart/
# https://github.com/ext0/RRISD-HAC-Reminders/blob/master/RRISD-HAC-Access/HAC.cs
# https://stackabuse.com/python-modules-creating-importing-and-sharing/

from getpass import getpass
import requests
# I'm using Python 3.7 on Windows and Python 3.8 on macOS to develop this program. Python 2.7 doesn't work. I have not tested it on other versions, so your mileage may vary on a different version.

# You probably don't want to edit these variables... Seriously, though, don't do it.
# You also probably won't want to edit the functions.
username = ""
password = ""
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'lis-hac.eschoolplus.powerschool.com', 'Origin': 'https://lis-hac.eschoolplus.powerschool.com', 'Referer': 'https://lis-hac.eschoolplus.powerschool.com/HomeAccess/Account/LogOn?ReturnUrl=%2fHomeAccess', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14.6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
cookies = {}

def getUserCreds():
    getUserCreds.username = input("Enter your username: ")
    getUserCreds.err1 = 0
    if getUserCreds.username == "":
        print("Username cannot be blank.")
        getUserCreds.err1 = 1
        getUserCredsErr(1)

    getUserCreds.password = getpass("Enter your password. (Your password is hidden.)")
    getUserCreds.err2 = 0
    if getUserCreds.password == "":
        print("Password cannot be blank.")
        err2 = 1
        getUserCredsErr(2)

def getUserCredsErr(jump):
    if jump == 1:
        getUserCredsErr.username = input("Enter your username: ")
        if getUserCredsErr.username == "":
            print("Username cannot be blank.")
            getUserCredsErr(1)
            
    if jump == 2:    
        getUserCredsErr.password = getpass("Enter your password. (Your password is hidden.) ")
        if getUserCredsErr.password == "":
            print("Password cannot be blank.")
            getUserCredsErr(2)

def saveForm():
    array = {'SCKTY00328510CustomEnabled': 'False', 'Database': 10}

    if getUserCreds.err1 == 1:
        array['LogOnDetails.UserName'] = getUserCredsErr.username
    else:
        array['LogOnDetails.UserName'] = getUserCreds.username

    if getUserCreds.err2 == 1:
        array['LogOnDetails.Password'] = getUserCredsErr.password
    else:
        array['LogOnDetails.Password'] = getUserCreds.password
    return array

def login(HAC, formdata, headers):
    login.r = requests.post(HAC.base + "HomeAccess/Account/LogOn?ReturnUrl=%2fHomeAccess", headers=headers, data=formdata)
    if "Your attempt to log in was unsuccessful." in login.r.text:
        print(login.r.text)
        raise NameError("Your attempt to log in was unsuccessful. Did you enter your username and password correctly?")
    saveCookies(login.r)

def saveCookies(r):
    cookies = login.r.cookies
    print("Saved cookies to variable cookies")
