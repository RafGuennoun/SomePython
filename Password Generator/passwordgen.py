import string
import random

def gen():

    s1 = string.ascii_uppercase
    # get a string of alphabets from A to Z in uppercase
    # print(s1)

    s2 = string.ascii_lowercase
    # get a string of alphabets from a to z in lowercase
    # print(s2)

    s3 = string.digits
    # get a string of numbers from 0 to 9
    # print(s3)

    s4 = string.punctuation
    # get a string of special caracteres
    # print(s4)

    passlen = int(input("Enter the passwod length\n"))

    # Create a list
    s = []

    # Add the elements of s1, s2, s3, s4 to the list
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    # Shuffle the list randomly
    random.shuffle(s)

    password = ("".join(s[0:passlen]))

    print(password)

gen()