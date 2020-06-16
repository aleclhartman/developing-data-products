from flask import Flask, render_template, request

import numpy as np

from model import predict

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

@app.route('/order-pizza')
def show_order_pizza_form():
    return render_template('order-pizza-form.html')

@app.route('/order-pizza', methods=['POST'])
def handle_pizza_order_submission():

    topping1 = request.form['topping1']
    topping2 = request.form['topping2']
    pizza = f'{topping1} and {topping2}'

    return f'One pizza with {pizza} on the way!'

@app.route('/count-to')
def count_to():
    return render_template('counting-form.html')

@app.route('/count-to', methods=['POST'])
def handle_counting_form_submission():
    n = int(request.form['n'])
    numbers = range(1, n + 1)

    return render_template(
        'counting-results.html',
        numbers=numbers
    )

@app.route('/predict-spam-ham')
def predict_spam_ham():
    return render_template('prediction-form.html')

@app.route('/predict-spam-ham', methods=['POST'])
def handle_prediction_form_submission():
    message = request.form["message"]
    spam_or_ham = predict(message)
    return f'This message is {spam_or_ham}'