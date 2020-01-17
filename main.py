## main.py - Code by Jannik Meier

# Import der Libraries (Flask und wines.py)
from flask import Flask, render_template, request, redirect
from libs.wines import *

app = Flask('mywines')

# Root Route (Startseite)
@app.route('/')
def home():
    return render_template('index.html', wines=load_wines())

# Weinkeller Route
@app.route('/cellar')
def cellar():
    return render_template('cellar.html', wines=load_wines())

# Weindetail Route
@app.route('/detail/<id>')
def detail(id):
    return render_template('detail.html', wine=load_wine_by_id(id))

# Route für Seite, um Wein hinzuzufügen
@app.route('/add', methods=['GET'])
def add():
    return render_template('add.html')

# Hier wird der POST abgefangen und der Wein hinzugefügt, danach nach /add weitergeleitet
@app.route('/add', methods=['POST'])
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

# Reine "technische" Seite - hier wird ein Wein anhand seiner ID gelöscht, danach wird zum Weinkeller weitergeleitet
@app.route('/delete/<id>', methods=['GET'])
def delete(id):
    delete_wine(id)
    return redirect('/cellar', code=302)

# Hier wird der Wine Pairing POST abgefangen - der Suchbegriff aus dem Request wird in die Funktion match_wines_to_meal(meal) eingesetzt und zurück ins Template kommt eine Liste mit Weinempfehlungen
@app.route('/winepairing', methods=['POST'])
def winepairing_search():
    meal = request.form['meal']
    matching_wines = match_wines_to_meal(meal)
    return render_template('winepairing.html', wines=matching_wines)

# Route für die Wine Pairing Seite
@app.route('/winepairing')
def winepairing_overview():
    return render_template('winepairing.html')

# Route für die Info Seite
@app.route('/info')
def info():
    return render_template('info.html')

# Starten des Servers
if __name__ == '__main__':
    app.run(debug=True, port=5000)