import os
import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def read_csv(file_path):
    products = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products

def read_sql():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    products = [{"id": row[0], "name": row[1], "category": row[2], "price": row[3]} for row in rows]
    conn.close()
    return products

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    products = []
    error = None

    if source == 'json':
        try:
            products = read_json('products.json')
        except Exception as e:
            error = f"Error reading JSON file: {e}"
    elif source == 'csv':
        try:
            products = read_csv('products.csv')
        except Exception as e:
            error = f"Error reading CSV file: {e}"
    elif source == 'sql':
        try:
            products = read_sql()
        except Exception as e:
            error = f"Error reading SQLite database: {e}"
    else:
        error = "Wrong source. Please specify 'json', 'csv', or 'sql'."

    if product_id and not error:
        products = [product for product in products if product['id'] == product_id]
        if not products:
            error = "Product not found."

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
