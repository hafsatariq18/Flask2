from sqlalchemy import create_engine, text
db_connection_string = "mysql+pymysql://admin:darkspell@database-1.cxg6uyogcz4r.us-east-2.rds.amazonaws.com/project?charset=utf8mb4"

engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
           "ssl_ca": "/etc/ssl/cert.pem"
        }
    })
def add_ord_to_db(product_id, data):
  with engine.connect()as conn:
    query = text ("INSERT INTO orders (product_id, full_name, address, pincode, payment_mode) VALUES (:product_id, :full_name, :address, :pincode, :payment_mode)")
    conn.execute (query,{
                     'product_id': product_id,
                     'full_name' : data ['full_name'],
                     'address' : data ['address'],
                     'pincode' : data ['pincode'],
                     'payment_mode' : data ['payment_mode']})