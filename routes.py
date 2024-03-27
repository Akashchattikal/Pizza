from flask import Flask, render_template, request, redirect, url_for, abort, \
    session

import sqlite3

app = Flask(__name__)


# @app.route("/")
# def home():
#     conn = sqlite3.connect('pizza.db')
#     cur = conn.cursor()
#     cur.execute('SELECT * FROM Pizza')
#     pizzas = cur.fetchall()
#     return render_template("all-pizzas.html", pizzas=pizzas)

# @app.route("/pizza/<int:id>")
# def single_pizza(id):
#     conn = sqlite3.connect('pizza.db')
#     cur = conn.cursor()
#     cur.execute('SELECT * FROM Pizza WHERE id = ?', (id,))
#     pizza = cur.fetchone()
#     return render_template("pizza.html", pizza=pizza)


@app.route("/")
def home():
    return render_template("home.html", title="Home Page")


@app.route("/all-pizzas")
def all_pizzas():
    conn = sqlite3.connect('pizza.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM Pizza')
    pizzas = cur.fetchall()
    return render_template("all-pizzas.html", pizzas=pizzas)


@app.route("/pizza/<int:id>")
def Pizza(id):
    conn = sqlite3.connect('pizza.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM Pizza WHERE id = ?', (id,))
    pizza = cur.fetchone()
    return render_template('pizza.html', pizza=pizza)


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)