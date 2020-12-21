# install the requests package with the command
# pip install requests
# we will use this package to sned and get data from websites

# install the win10toast with the command
# pip install win10toast
# this package will help us to show the notification in the notifications area in windows 10

import requests
from win10toast import ToastNotifier
import json
import time

def update():
    print("updating ...")
    # The api site
    r = requests.get("https://coronavirus-19-api.herokuapp.com/all")

    # The variable data will contain the json tree
    data = r.json()

    # Setting the variable text with the informations from data
    text = f'Confirmed cases : {data["cases"]} \nDeaths : {data["deaths"]} \nRecovered : {data["recovered"]}'

    while True:
        # Create the notifier
        toast = ToastNotifier()

        # Show the notification
        toast.show_toast("Covid-19 Updates", text, duration=10)

        print("shown .. !!")

        # Show the notification every hour
        time.sleep(60)

update()

# Make sure that the notifications on your pc are enabled
# Or this program will not work

# To enable the notifications in windows 10 :
    # At the bottom right corner, click the Action Center botton
    # In the Actions Center, in the top right corner, click on "Manage notifications"
    # Enable notifications
