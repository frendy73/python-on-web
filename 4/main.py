from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world from Flask!"

@app.route('/search4')
def search4():
    random_json = {
        'random_number1': random.randint(1, 100),
        'random_number2': random.randint(1, 100)
    }
    return jsonify(random_json)

if __name__ == '__main__':
    app.run(debug=True)