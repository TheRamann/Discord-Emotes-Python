import requests


def smug():
    x = requests.get('https://nekos.life/api/v2/img/smug'
    return x.json()['url']


def hug():
    x = requests.get('https://nekos.life/api/v2/img/hug')
    return x.json()['url']


def kiss():
    x = requests.get('https://nekos.life/api/kiss')
    return x.json()['url']


def pat():
    x = requests.get('https://nekos.life/api/v2/img/pat')
    return x.json()['url']


def poke():
    x = requests.get('https://nekos.life/api/v2/img/poke')
    return x.json()['url']


def slap():
    x = requests.get('https://nekos.life/api/v2/img/slap')
    return x.json()['url']


def tickle():
    x = requests.get('https://nekos.life/api/v2/img/tickle')
    return x.json()['url']


def neko():
    x = requests.get('https://nekos.life/api/neko')
    return x.json()['neko']


def ngif():
    x = requests.get('https://nekos.life/api/v2/img/ngif')
    return x.json()['url']


def cuddle():
    x = requests.get('https://nekos.life/api/v2/img/cuddle')
    return x.json()['url']
