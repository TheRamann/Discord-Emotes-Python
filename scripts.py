import requests


def smug():
    x = requests.get('https://nekos.life/api/v2/img/smug')
    print(x.json()['url'])


def hug():
    x = requests.get('https://nekos.life/api/v2/img/hug')
    print(x.json()['url'])


def kiss():
    x = requests.get('https://nekos.life/api/kiss')
    print(x.json()['url'])


def pat():
    x = requests.get('https://nekos.life/api/v2/img/pat')
    print(x.json()['url'])


def poke():
    x = requests.get('https://nekos.life/api/v2/img/poke')
    print(x.json()['url'])


def slap():
    x = requests.get('https://nekos.life/api/v2/img/slap')
    print(x.json()['url'])


def tickle():
    x = requests.get('https://nekos.life/api/v2/img/tickle')
    print(x.json()['url'])


def neko():
    x = requests.get('https://nekos.life/api/neko')
    print(x.json()['neko'])


def ngif():
    x = requests.get('https://nekos.life/api/v2/img/ngif')
    print(x.json()['url'])


def cuddle():
    x = requests.get('https://nekos.life/api/v2/img/cuddle')
    print(x.json()['url'])