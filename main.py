# name, year, size, meals, grape, region, pricepaid

from flask import Flask, render_template, request
import json

app = Flask("mywines")

# Routes

@app.route('/')
@app.route('/index')
def overview():
    return render_template("index.html", wines=load_wines())

@app.route('/detail/<id>')
def detail(id):
    return render_template("detail.html", wine=load_wine_by_id(id))

@app.route('/add', methods=["GET"])
def add():
    return render_template("add.html")

@app.route("/add", methods=["POST"]) # Post abfangen und Wein hinzufügen
def add_post():
    add_new_wine(request.form['name'], request.form['year'], request.form['size'], request.form['meals'], request.form['grape'], request.form['region'], request.form['pricepaid'])
    return render_template("add.html")

# Weinverwaltung

def load_wine_by_id(id):
    wines = load_wines()
    for wine in wines:
        print(wine)
        if int(wine["id"]) == int(id):
            return wine
    return None

def add_new_wine(name, year, size, meals, grape, region, pricepaid):
    wines = load_wines()
    wines.append({
        "name": name,
        "year": year,
        "size": size,
        "meals": meals,
        "grape": grape,
        "region": region,
        "pricepaid": pricepaid
    })

    save_wines(wines)

def load_wines():
    with open('data.json', 'r') as json_file:
        return json.load(json_file)

def save_wines(wines):
    with open('data.json', 'w') as outfile:
        json.dump(wines, outfile)

# Hochfahren des Servers

if __name__ == "__main__":
    app.run(debug=True, port=5000)