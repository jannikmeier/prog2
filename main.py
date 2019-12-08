from flask import Flask, render_template, request
import json

app = Flask("hello")

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/overview')
def overview():
    return render_template("overview.html", wines=load_wines())

@app.route('/detail/<id>')
def detail(id):
    return render_template("detail.html", wine=load_wine_by_id(id))

@app.route('/add', methods=["GET"])
def add():
    return render_template("add.html")

@app.route("/add", methods=["POST"])
def add_post():
    add_new_wine(request.form['name'], request.form['year'], request.form['size'])
    return render_template("add.html")



def load_wine_by_id(id):
    wines = load_wines()
    for wine in wines:
        print(wine)
        if int(wine["id"]) == int(id):
            return wine
    return None

def add_new_wine(name, year, size):
    wines = load_wines()
    wines.append({
        "name": name,
        "year": year,
        "size": size
    })

    save_wines(wines)

def load_wines():
    with open('data.json', 'r') as json_file:
        return json.load(json_file)

def save_wines(wines):
    with open('data.json', 'w') as outfile:
        json.dump(wines, outfile)

if __name__ == "__main__":
    app.run(debug=True, port=5000)