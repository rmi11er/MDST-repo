"""
MDST Workshop 1 - Python Basics Starter Code
"""

# Add any imports you need here:
import random
import base64

def part1(num):
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """
    response = input("Input some number!")
    if (response % 2 == 1):
        print("Your number is odd!")
    else:
        print("Your number is even")


def part2():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """
    exit = False
    guessed_it = False

    while(exit != True):
        num = random.randint(1, 9)
        while guessed_it != True:
            guess = input("Try and guess my number...")
            if (int(guess) == num):
                print("You guessed it!")
                guessed_it = True
                continue
            elif (int(guess) > num):
                print("Too high!")
            elif(guess == "Exit"):
                exit = True
            else:
                print("Too low!")
        meow = raw_input("Exit or Continue?")
        if meow == "Exit":
            exit = True
        else:
            guessed_it = False


def part3(string):
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """
    str = raw_input("Send me a string!")
    str_r = str[::-1]

    if (str == str_r):
        print("that's a palindrome!")
    else:
        print("that is not a palindrome!")


def part4a(filename, username, password):
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """
    encodedUserBytes = base64.b64encode(username.encode("utf-8"))
    encodedPassBytes = base64.b64encode(password.encode("utf-8"))
    encodedUserStr = str(encodedUserBytes)
    encodedPassStr = str(encodedPassBytes)

    with open(filename, "a") as f:
        f.write(encodedUserStr)
        f.write("\n")
        f.write(encodedPassStr)



def part4b(filename, password=None):
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """
    with open(filename, "r") as f:
        print str(f)
        f.close()

    if password:
        with open(filename, "a") as f2:
            encodedNewPass = base64.b64encode(password.encode("utf-8"))
            encodedStrPass = str(encodedNewPass)
            f2.write(encodedStrPass)

if __name__ == "__main__":
    part1(3)  # odd!
    part1(4)  # even!
    part2()
    part3("ratrace")  # False
    part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")
