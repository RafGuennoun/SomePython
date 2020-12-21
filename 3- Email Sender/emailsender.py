import smtplib

# Contains the email that we will send to
to = input("Email of the recepient : \n")

# Content
content = input("The content of the email : \n")

# My emailadress
myEmailAdress = "exemple@gmail.com"

# My email password
myEmailPassword = "1234"

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)

    # Make the connection with smtp gmail
    server.ehlo()

    # Start the session
    server.starttls()

    # Login to gmail
    # server.login('senderemail@gmail.com', 'password')
    server.login(myEmailAdress, myEmailPassword)

    # Send the email
    server.sendmail(myEmailAdress, to, content)

    # Close the smtp server
    server.close()

sendEmail(to, content)