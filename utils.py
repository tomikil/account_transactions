import requests


def load_word():
    word = requests.get('https://api.npoint.io/84a13bf5a750a2e2c7cd')
    words = word.json()
    return words


