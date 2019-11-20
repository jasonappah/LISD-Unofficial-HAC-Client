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
username = "jason.antwiappah35@k12.leanderisd.org"
password = "Jason5002"
formdata = ""
headers = {'user_agent':'Mozilla/5.0 Gecko Firefox', 'Accept-Language': 'en-US,en;q=0.9', 'Upgrade-Insecure-Requests': '1', 'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate, br','Cache-Control': 'max-age=0', 'Referer': 'https://lis-hac.eschoolplus.powerschool.com/HomeAccess/Account/LogOn', 'Connection': 'keep-alive', 'Cookie': 'SPIHACSiteCode=; ASP.NET_SessionId=0u2rrjwtef0dheynebtusdwx; BIGipServerLIS-ESP-HAC_Pool=236720812.47873.0000', 'Sec-Fetch-User': '?1'}
html = ""

def getUserCredsErr(jump):
    if jump == 1:
        username = input("Enter your username: ")
        if username == "":
            print("Username cannot be blank.")
            getUserCredsErr(1)
            
    if jump == 2:    
        password = getpass("Enter your password. (Your password is hidden.) ")
        if password == "":
            print("Password cannot be blank.")
            getUserCredsErr(2)

def getUserCreds():
    username = input("Enter your username: ")
    if username == "":
        print("Username cannot be blank.")
        getUserCredsErr(1)

    password = getpass("Enter your password. (Your password is hidden.)")
    if password == "":
        print("Password cannot be blank.")
        getUserCredsErr(2)

def login(HAC, formdata):
    print("Attempting to login")
    r = requests.post(HAC.base + "/HomeAccess/Home/WeekView", headers=headers, data=formdata)
    print("Testing if login was successful")
    print (r.url)
    html = r.text
    if html != "":
        print (html)
        return 1 # it worked
    else: 
        print("Something went wrong. Did you enter your login details correctly.")
        return 0 # something wrong