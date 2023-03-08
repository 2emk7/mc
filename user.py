import requests
import time

with open('usernames.txt', 'r') as file:
    usernames = file.read().splitlines()

delay = 1.05

for username in usernames:
    response = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{username}')

    if response.status_code == 204:
        print(f'{username} is available!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        
        with open('available_usernames.txt', 'a') as file:
            file.write(f'{username}\n')
    else:
        print(f'{username} is not.')
    
    time.sleep(delay)