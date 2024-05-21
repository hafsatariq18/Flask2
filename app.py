from flask import Flask, render_template, jsonify
app = Flask(__name__)

PRODUCTS=[
    {'id': 1,
    'item': 'Shea Shower Cream',
    'skin_type': 'Dry Skin',
    'use': 'Cleanse and help soften'},

    {'id': 2,
    'item': 'Almond Milk Shower Cream',
    'skin_type': 'Dry Skin',
    'use': 'Cleanse, help soften and Comfort'},

    {'id': 3,
    'item': 'Olive Body Butter',
    'skin_type': 'Very Dry Skin',
    'use':'Help soften.96 Hrs Moisture'}

]

@app.route("/")
def hello_world():
    return render_template('home.html',products=PRODUCTS)

@app.route("/api/products")
def list_products():
    return jsonify(PRODUCTS)

if __name__ ==  "__main__": 
    app.run(host='0.0.0.0',port=8080, debug=True)