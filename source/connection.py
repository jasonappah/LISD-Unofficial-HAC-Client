# Maybe these useful links will help jog your mind and let you figure out what it is you were doing last night.
# r = requests.post("https://httpbin.org/post", data=main.formdata)
# https://3.python-requests.org/user/quickstart/
# https://github.com/ext0/RRISD-HAC-Reminders/blob/master/RRISD-HAC-Access/HAC.cs
# https://stackabuse.com/python-modules-creating-importing-and-sharing/

from getpass import getpass
# I'm using Python 3.7 on Windows and Python 3.8 on macOS to develop this program. I have not tested it on other versions, so your mileage may vary on a different version.

# You probably don't want to edit these variables... Seriously, though, don't do it.
# You also probably won't want to edit the functions.
r = ""
username = ""
password = ""
formdata = ""

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

