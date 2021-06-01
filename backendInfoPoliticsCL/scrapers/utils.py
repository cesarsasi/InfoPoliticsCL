import requests


def get_session():
    session = requests.Session()
    return session