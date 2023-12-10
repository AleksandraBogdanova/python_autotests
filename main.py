import requests


response = requests.post(url="https://api.pokemonbattle.me:9104/trainers/reg", 
                         json={
                             "trainer_token": "d598ef4109d396a913aa2ffcd3e66677",
                             "email": "bogdanova466@yandex.ru",
                             "password": "Iloveqa1"},
                         headers={'Content-Type': 'application/json'}, timeout=5)

print(f'Code: {response.status_code} - {response.reason}. Message:{response.text} ')

if response.status_code == 200:
    print('Ok!')
else: 
    print("Bad!")

response = requests.post(url="https://api.pokemonbattle.me:9104/trainers/confirm_email", 
                         json={
                             "trainer_token": "d598ef4109d396a913aa2ffcd3e66677"},
                         headers={'Content-Type': 'application/json'}, timeout=5)

print(f'Code: {response.status_code} - {response.reason}. Message:{response.text} ')

if response.status_code == 200:
    print('Ok!')
else: 
    print("Bad!")

response = requests.post(url="https://api.pokemonbattle.me:9104/pokemons", 
                         json={
                             "name": "Бульбазавr",
                             "photo": "https://dolnikov.ru/pokemons/albums/001.png"},
                         headers={'Content-Type': 'application/json', 'trainer_token': 'd598ef4109d396a913aa2ffcd3e66677'}, timeout=5)

print(f'Code: {response.status_code} - {response.reason}. Message:{response.text} ')

if response.status_code == 200:
    print('Ok!')
else: 
    print("Bad!")

response = requests.post(url="https://api.pokemonbattle.me:9104/pokemons", 
                         json={
                              "pokemon_id": "21529",
                              "name": "New Name",
                              "photo": "https://dolnikov.ru/pokemons/albums/008.png"
},
                         headers={'Content-Type': 'application/json', 'trainer_token': 'd598ef4109d396a913aa2ffcd3e66677'}, timeout=5)

print(f'Code: {response.status_code} - {response.reason}. Message:{response.text} ')

if response.status_code == 200:
    print('Ok!')
else: 
    print("Bad!")

response = requests.post(url="https://api.pokemonbattle.me:9104/trainers/add_pokeball", 
                         json={"pokemon_id": "21529"},
                         headers={'Content-Type': 'application/json', 'trainer_token': 'd598ef4109d396a913aa2ffcd3e66677'}, timeout=5)

print(f'Code: {response.status_code} - {response.reason}. Message:{response.text} ')

if response.status_code == 200:
    print('Ok!')
else: 
    print("Bad!")