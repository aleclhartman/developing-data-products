from flask import Flask

import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/roll-dice')
def roll_dice():
    roll1 = np.random.choice(range(1, 7))
    roll2 = np.random.choice(range(1, 7))
    roll3 = np.random.choice(range(1, 7))
    return (f'''Dice one: {roll1}, \n
            Dice two: {roll2}, \n
            Dice three: {roll3}''')