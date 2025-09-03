import requests
import sqlite3


class extract:

    def __init__(self):
        pass
    
url = "http://universities.hipolabs.com/search?country=Brazil"

# Acessando o link da internet
response = requests.get(url)
response.raise_for_status()  
universities = response.json()