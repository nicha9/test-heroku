from flask import Flask, request
# import pyrebase  #pip install pyrebase4


app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"


if __name__ == '__main__':
    app.run(debug=True)