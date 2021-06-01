import sys
from scrapers import ciper
from flask import Flask

app = Flask(__name__)

def run_scraper(name):
    if name == 'ciper':
        print('hola')
        return ciper()

@app.route('/')
def prueba():
    return "Hola"

if __name__ == '__main__':
    app.run(debug = True)
