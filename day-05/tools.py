from datetime import datetime
import random
import secrets
import string

def get_current_time():
    # tool to get current time
    """Tool to return current date and time"""
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S %p")

def roll_dice():
    # Tool to roll dice
    return random.randint(1,6)

def generate_password(length=12):
    # Tool to generate password
    password = [secrets.choice(string.ascii_uppercase),secrets.choice(string.ascii_lowercase),
                secrets.choice(string.punctuation), secrets.choice(string.digits) ]
    all_character = string.ascii_letters+string.punctuation+string.digits
    password += [secrets.choice(all_character) for _ in range(length-4)]
    return "".join(password)


# Tool to read file and handle error gracefully
def read_file(filename):
    # Tool to read the file from local system available in data folder
    # try:
        with open(filename, "r") as file:
            content = file.read()
            return content
    # except FileNotFoundError:
        # return "Error: File not found"
    