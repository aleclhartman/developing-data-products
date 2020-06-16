from flask import Flask, render_template

import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    message = 'Hello, World!'
    return render_template('home_page.html', message=message)

@app.route('/roll-dice/<int:n>')
def roll_dice(n):

    rolls = [str(np.random.choice(range(1, 7))) for i in range(n)]

    return render_template('roll_dice.html', rolls=rolls)

@app.route('/say/<greeting>/to/<name>')
def sayhelloto(greeting, name):
    message = f'{greeting}, {name}!'
    return render_template('greeting.html', message=message)