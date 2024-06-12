from flask import Flask, render_template, jsonify, request
from database import engine, add_ord_to_db
from sqlalchemy import text

app = Flask(__name__)

def get_product_by_id(product_id):
    products = load_products()
    for product in products:
        if product['id'] == product_id:
            return product
    # return None

def load_products():
        with engine.connect() as conn:
            result = conn.execute(text("select * from PRODUCTS"))
            rows = result.fetchall()
            product_list = [{'id': row[0], 'item': row[1], 'skin_type': row[2], 'uses': row[3], 'price': row[4]} for row in rows]
            return product_list
         

@app.route("/")
def hello_world():
    products = load_products()
    # print(f"Loaded products: {products}")
    return render_template('home.html', products=products)

@app.route("/api/products")
def list_products():
    products = load_products()  # Fetch the list of products
    return jsonify(products) 

@app.route("/product/<int:product_id>")
def product_detail(product_id):
    product = get_product_by_id(product_id)
    if product:
        return render_template('product_detail.html', product=product)
    else:
        return "Product not found", 404

@app.route("/buy_now/<int:product_id>")
def buy_now(product_id):
    product = get_product_by_id(product_id)
    if product:
        return render_template('form.html', product=product)
    else:
        return "Product not found", 404

@app.route("/buy_now/<int:product_id>/place_order", methods=["POST"])
def place_order(product_id):
    data = request.form
    product = get_product_by_id(product_id)
    if product:
        add_ord_to_db(id, data)
        return render_template('order_details.html', **request.form, order_status='Order Placed', product=product, orders=data)
        print(data)
    else:
        return "Product not found", 404

  


if __name__ ==  "__main__": 
    app.run(host='0.0.0.0',port=8080, debug=True)