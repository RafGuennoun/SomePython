# This program is for lazy poeple
# Just kidding ...
# It will help you save lot of time

import webbrowser as wb

def webauto():

    # We will work with the default browser in your pc
    # For exemple if Chrome is your default browser the links will open in Chrome

    # Setting the list of urls that we want to open
    URLS = (
        "https://www.google.com",
        "https://www.youtube.com",
        "https://www.gmail.com",
        "https://www.facebook.com",
        "https://www.messenger.com",
        "https://www.instagram.com",
        "https://www.linkedin.com/in/raf-guennoun/"
    )

    # Open the urls
    for url in URLS:
        print("Opening : "+ url)

        # Open the url
        wb.open(url)

webauto()