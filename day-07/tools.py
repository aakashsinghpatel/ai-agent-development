from datetime import datetime
import random
import secrets
import string

def get_current_time():
    """Tool to return current date and time"""
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S %p")

def roll_dice():
    """ generate nuber for roll dice """
    return random.randint(1,6)

def generate_password(length=12):
    """ Generate passeord randomly """
    password = [secrets.choice(string.ascii_uppercase),secrets.choice(string.ascii_lowercase),
                secrets.choice(string.punctuation), secrets.choice(string.digits) ]
    all_character = string.ascii_letters+string.punctuation+string.digits
    password += [secrets.choice(all_character) for _ in range(length-4)]
    return "".join(password)
    