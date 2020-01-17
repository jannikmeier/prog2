## wines.py - Code by Jannik Meier

# Import der Libraries
import json
import uuid
import datetime

# Funktion, die den Wein anhand seiner ID zurückgibt
def load_wine_by_id(id):
    wines = load_wines()
    for wine in wines:
        if str(wine["id"]) == str(id):
            return wine
    return None

# Funktion, die einen neuen Wein ins JSON-File hinzufügt
# Als ID wird eine UUID verwendet
# Gerichte werden durch ihre Kommas gesplittet und in eine Liste hinzugefügt
# Die Trinkreife wird gleich beim Hinzufügen mittels der Funktion winematurity(year, grape) berechnet
def add_new_wine(name, year, size, meals, grape, region, pricepaid):
    wines = load_wines()
    wines.append({
        "id": str(uuid.uuid1()),
        "name": name,
        "year": year,
        "size": size,
        "meals": [meal.strip() for meal in meals.split(',')],
        "grape": grape,
        "winematurity": winematurity(year, grape),
        "region": region,
        "pricepaid": pricepaid
    })
    save_wines(wines)

# Funktion, die alle Weine aus dem JSON zurückgibt
def load_wines():
    with open('data.json', 'r') as json_file:
        return json.load(json_file)

# Funktion, die alle Weine im JSON-File speichert
def save_wines(wines):
    with open('data.json', 'w') as outfile:
        json.dump(wines, outfile)

# Funktion, die einen Wein anhand seiner ID aus dem JSON-File löscht
# Hierzu werden alle Weine geladen und es wird durch sie geloopt bis der richtige Wein anhand seiner ID gefunden wird
# Folglich wird der Wein aus der Liste entfernt und die Weine werden mit save_wines() wieder gespeichert
def delete_wine(id):
    wines = load_wines()
    for wine in wines:
        if str(wine["id"]) == str(id):
            wines.remove(wine)
    save_wines(wines)
    return None

# Funktion, die das Wine Matching macht
# Hierzu werden alle Wine mittels Funktion load_wines() geladen und eine leere Liste matching_wines bereitgestellt
# Als Input dient ein Gericht (searched_meal), das der Funktion mitgegeben wird
# Es wird durch alle Weine aus dem Weinkeller geloopt, darin wird durch alle Gerichte "innerhalb" jedes Weines geloopt
# Sobald es einen Match gibt und ein Gericht aus einem Wein mit dem gesuchten Gericht übereinstimmt, wird der Wein in die List "matching_wines" hinzugefügt
# Zurückgegeben wird die Liste mit allen "gematchten" Weinen
def match_wines_to_meal(searched_meal):
    all_wines = load_wines()
    matching_wines = []
    for wine in all_wines:
        for meals_per_wine in wine['meals']:
            if meals_per_wine == searched_meal:
                matching_wines.append(wine)
    return matching_wines

# Funktion, welche die Trinkreife eines Weines berechnet
# Hierzu definiere ich eine Liste mit einigen Traubensorten und nach wie vielen Jahren Wein mit jenen Trauben in etwa trinkreif sind (eigene Einschätzung, keine Garantie ;-P)
# Wenn eine Traubensorte eingegeben wird, die sich nicht in der Liste befindet, sagen wir einfach dass der Wein nach 2 Jahren trinkreif ist
# Schlussendlich wird das Jahrgang des Weins mit der Zeit zum Reifen addiert und wir haben das Jahr, in dem der Wein trinkreif ist
def winematurity(year, grape):
    grape_maturity = {
        'Tempranillo': 5,
        'Primitivo': 1,
        'Syrah': 3,
        'Merlot': 5,
        'Pinot Noir': 2,
        'Cabernet Sauvignon': 5,
        'Malbec': 5
    }
    years_to_add = grape_maturity.get(grape, 2)
    return int(year) + years_to_add