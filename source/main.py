# Maybe these useful links will help jog your mind and let you figure out what it is you were doing last night.
# r = requests.post("https://httpbin.org/post", data=main.formdata)
# https://3.python-requests.org/user/quickstart/
# https://github.com/ext0/RRISD-HAC-Reminders/blob/master/RRISD-HAC-Access/HAC.cs
# https://stackabuse.com/python-modules-creating-importing-and-sharing/

import connection
from HAC import *

# Customize the line below to use this for your own school. Your mileage may vary.
HAC = HAC("https://lis-hac.eschoolplus.powerschool.com/")

introMessage = "Welcome to uHAC!"

print(introMessage)
print("Testing if we can connect to " + HAC.fullURL)

if HAC.Avaliable(HAC.fullURL) == 1:
    print("We're good to go!")
else:
    print("We have a problem. Are you connected to the internet? I can't seem to reach your server.")
    raise NameError("Can't reach server")
    # I don't know if that single quote in the middle of the string is good practice. Do I need to escape it??

# connection.getUserCreds()

formdata = {'SCKTY00328510CustomEnabled': 'False', 'Database': 10, 'LogOnDetails.UserName': connection.username, 'LogOnDetails.Password': connection.password}
connection.login(HAC, formdata, connection.headers)