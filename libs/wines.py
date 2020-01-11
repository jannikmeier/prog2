import json
import uuid 

def load_wine_by_id(id):
    wines = load_wines()
    for wine in wines:
        if str(wine["id"]) == str(id):
            return wine
    return None

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

def load_wines():
    with open('data.json', 'r') as json_file:
        return json.load(json_file)

def save_wines(wines):
    with open('data.json', 'w') as outfile:
        json.dump(wines, outfile)

def delete_wine(id):
    wines = load_wines()
    for wine in wines:
        if str(wine["id"]) == str(id):
            wines.remove(wine)
    save_wines(wines)
    return None

def match_wines_to_meal(meal):
    wines = load_wines()
    matching_wines = []
    for wine in wines:
        for wine_meal in wine.meal:
            if wine_meal == meal:
                matching_wines.append(wine)
    return matching_wines

def winematurity(year, grape):
    grape_maturity = {
        'Tempranillo': 5,
        'Primitivo': 2,
        'Syrah': 3,
        'Merlot': 5,
        'Pinot Noir': 2,
        'Cabernet Sauvignon': 5,
        'Malbec': 5
    }
    years_to_add = grape_maturity.get(grape, 2)
    return int(year) + years_to_add