from flask import Flask, render_template, request, redirect
from libs.wines import *

app = Flask('mywines')

# Routes

@app.route('/')
def home():
    return render_template('index.html', wines=load_wines())

@app.route('/cellar')
def cellar():
    return render_template('cellar.html', wines=load_wines())

@app.route('/detail/<id>')
def detail(id):
    return render_template('detail.html', wine=load_wine_by_id(id))

@app.route('/add', methods=['GET'])
def add():
    return render_template('add.html')

@app.route('/add', methods=['POST']) # Post abfangen und Wein hinzufügen
def add_post():
    add_new_wine(
        request.form['name'],
        request.form['year'],
        request.form['size'],
        request.form['meals'],
        request.form['grape'],
        request.form['region'],
        request.form['pricepaid']
    )
    return redirect('/cellar', code=302)

@app.route('/delete/<id>', methods=['GET'])
def delete(id):
    delete_wine(id)
    return redirect('/cellar', code=302)

@app.route('/winepairing', methods=['POST'])
def winepairing_search():
    print(request.form)
    meal = request.form['meal']
    matching_wines = match_wines_to_meal(meal)
    return render_template('winepairing.html', wines=matching_wines)

@app.route('/winepairing', methods=['GET'])
def winepairing_overview():
    return render_template('winepairing.html')

@app.route('/info')
def info():
    return render_template('info.html')

# Starten des Servers

if __name__ == '__main__':
    app.run(debug=True, port=5000)