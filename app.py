import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, Romeo'

os.system("ls && nohup python3 -m Romeo &")
