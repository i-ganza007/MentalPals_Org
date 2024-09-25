from flask import Flask
from flask_pymongo import PyMongo , MongoClient
from dotenv import load_dotenv, find_dotenv
import os
from urllib.parse import quote_plus

load_dotenv(find_dotenv())
password = os.environ.get('MONGO_PWD')

encoded_password = quote_plus(password)


connection_string = f"mongodb+srv://ianganza4:{encoded_password}@cluster0.xat2t.mongodb.net/"


app = Flask(__name__)
app.config['SECRET_KEY'] = '34e67bd2d49d5bd03fd1'

app.config['MONGO_URI'] = connection_string
mongo = PyMongo(app)

client = MongoClient(connection_string)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
