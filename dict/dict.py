# this will be the main application
import requests
import functools
from bs4 import BeautifulSoup
from flask import Flask


app = Flask(__name__)

@app.route('/')

def dict():
    


    return 'Welcome!'