from ast import arg
from concurrent.futures import thread
import requests
from random import randint
from urllib.parse import urlencode
import threading
from colorama import Fore, Back
import time
import random
import secrets

global count
count = 0

def generate_complex_password(include_random_number=True):
    pet_names = ['Buddy', 'Molly', 'Max', 'Lucy', 'Charlie', 'Lola']
    objects = ['Table', 'Chair', 'Lamp', 'Book', 'Computer', 'Guitar']
    hobbies = ['Reading', 'Gardening', 'Cooking', 'Photography', 'Hiking', 'Painting']

    random.shuffle(pet_names)
    random.shuffle(objects)
    random.shuffle(hobbies)

    pet_name = secrets.choice(pet_names)
    obj = secrets.choice(objects)
    hobby = secrets.choice(hobbies)

    random_number = secrets.randbelow(100) if include_random_number else ''

    password_items = [pet_name, obj, hobby, str(random_number)]
    random.shuffle(password_items)
    password = ''.join(password_items)

    return password

def generate_gmail_address():
    first_names = [
        'Liam', 'Olivia', 'Noah', 'Emma', 'Sophia', 'Jackson', 'Aiden', 'Lucas', 'Oliver', 'Ava',
        'Isabella', 'Mia', 'Ethan', 'Layla', 'Harper', 'Caden', 'Amelia', 'Evelyn', 'Abigail', 'Ella',
        'Benjamin', 'Grayson', 'James', 'Michael', 'Daniel', 'Matthew', 'William', 'Alexander', 'Henry',
        'Charlotte', 'Mila', 'Aria', 'Scarlett', 'Zoe', 'Chloe', 'Ella', 'Grace', 'Lily', 'Lillian',
        'Sofia', 'Hazel', 'Luna', 'Penelope', 'Nora', 'Leah', 'Scarlett', 'Mila', 'Aria', 'Chloe',
        'Lily', 'Emma', 'Ella', 'Ava', 'Olivia', 'Sophia', 'Amelia', 'Harper', 'Evelyn', 'Abigail',
        'Mia', 'Isabella', 'Aiden', 'Liam', 'Noah', 'Lucas', 'Ethan', 'Oliver', 'Jackson', 'Caden',
        'Sebastian', 'Ezra', 'Mateo', 'Elijah', 'Grayson', 'Lincoln', 'Leo', 'Daniel', 'Matthew',
        'William', 'James', 'Michael', 'Benjamin', 'Henry', 'Alexander', 'Samuel', 'David', 'Joseph',
        'Nicholas', 'Avery', 'Grace', 'Scarlett', 'Mila', 'Aria', 'Chloe', 'Lily', 'Zoe', 'Ella'
    ]
    selected_name = random.choice(first_names)

    random_number = ''.join(random.choice('0123456789') for _ in range(8))
    separator = random.choice(['.', '_', ''])

    gmail_address = f'{selected_name}{separator}{random_number}@gmail.com'
    return gmail_address


def getAccessToken():
    url = 'https://api.likesjet.com/users/create'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    email = generate_gmail_address()
    password = generate_complex_password()

    data = {
        'email': email,
        'password': password,
        'retype_password': password
    }

    print(f'{Back.BLUE} i  {Back.RESET}{Fore.WHITE} ► {Fore.BLUE}Got E-Mail address: {Fore.CYAN}{email}{Fore.RESET}')

    req = requests.post(url = url, headers = headers, json = data)

    return req.json()['accessToken']

def boostFollowers(name: str):

    global count

    while True:
        try:
            accessToken = getAccessToken()
        except:
            print(f'{Back.RED} !  {Back.RESET}{Fore.WHITE} ► {Fore.LIGHTRED_EX}Error: Access Token not created (network issue?)')
            time.sleep(1)
            continue
        break

    print(f'{Back.GREEN} ✔  {Back.RESET}{Fore.WHITE} ► {Fore.BLUE}Created session token: {Fore.CYAN}{accessToken[0:100]}...{Fore.RESET}')

    url = 'https://api.likesjet.com/addboost/2'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Authorization': f'Bearer {accessToken}'
    }

    data = {
        'coins_per_unit': '10',
        'required': '100',
        'service_id': 2,
        'tiktok_username': @steemaxx
    }

    while True:
        try:
            req = requests.post(url = url, headers = headers, json = data)
        except:
            print(f'{Back.RED} !  {Back.RESET}{Fore.WHITE} ► {Fore.LIGHTRED_EX}Error: Post Request failed (network issue?)')
            time.sleep(1)
            continue
        break

    if req.json()['status'] == True:
        count += 1
        print(f'{Back.GREEN} ✔  {Back.RESET}{Fore.WHITE} ► {Fore.BLUE}Sent followers {Fore.CYAN}[Status: {Fore.GREEN}True{Fore.CYAN}, {Fore.GREEN}User: {name}{Fore.CYAN}, {Fore.GREEN}Count: {count}{Fore.CYAN}]{Fore.RESET}')
        time.sleep(15)
    else:
        print(f'{Back.RED} !  {Back.RESET}{Fore.WHITE} ► {Fore.LIGHTRED_EX}Cooldown: 15 seconds')
        print(req.json())
        time.sleep(15)
        


input_name = input(f'{Back.BLUE} ?  {Back.RESET}{Fore.WHITE} ► {Fore.BLUE}Enter Username: {Fore.CYAN}')
while True:
    boostFollowers(name = input_name)
