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

def magicSauce(link):
    data = {
        'scene': 2,
        'platform_id': 'copy',
        'share_url': link
    }

    url = f'https://api31-normal-useast2a.tiktokv.com/tiktok/share/link/shorten/v1/?device_platform=android&os=android&ssmix=a&channel=googleplay&aid=1233&app_name=musical_ly&version_code=320706&version_name=32.7.6&manifest_version_code=2023207060&update_version_code=2023207060&ab_version=32.7.6&resolution=1600*900&dpi=320&device_type=SM-N976N&device_brand=samsung&language=de&os_api=32&os_version=12&ac=wifi&is_pad=0&current_region=DE&app_type=normal&sys_region=DE&timezone_name=Africa%2FBrazzaville&carrier_region_v2=262&residence=BE&app_language=de&carrier_region=BE&timezone_offset=3600&host_abi=arm64-v8a&locale=de-DE&ac2=wifi5g&uoo=0&op_region=BE&build_number=32.7.6&region=DE&iid=7318742228145800993&device_id=6636912843981686277&{urlencode(data)}'

    headers = {
        'Host': 'api31-normal-useast2a.tiktokv.com',
        'User-Agent': 'com.zhiliaoapp.musically/2023207060 (Linux; U; Android 12; de_DE; SM-N976N; Build/QP1A.190711.020;tt-ok/3.12.13.4-tiktok)'
    }

    req = requests.post(url = url, headers = headers, json = data)
    return req.json()['shorten_url']

def boostLikes(link: str):

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

    url = 'https://api.likesjet.com/addboost/1'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Authorization': f'Bearer {accessToken}'
    }

    link = magicSauce(link)

    data = {
        'coins_per_unit': '10',
        'required': '10',
        'service_id': 1,
        'link': link
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
        print(f'{Back.GREEN} ✔  {Back.RESET}{Fore.WHITE} ► {Fore.BLUE}Sent like lol {Fore.CYAN}[Status: {Fore.GREEN}True{Fore.CYAN}, {Fore.GREEN}Link: {link}{Fore.CYAN}, {Fore.GREEN}Count: {count}{Fore.CYAN}]{Fore.RESET}')
        time.sleep(8)
    else:
        time.sleep(8)
        


input_link = input(f'{Back.BLUE} ?  {Back.RESET}{Fore.WHITE} ► {Fore.BLUE}Enter Link: {Fore.CYAN}')
while True:
    boostLikes(link = input_link)
