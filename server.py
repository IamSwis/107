from flask import Flask, request
import json


app = Flask(__name__)# This is the name of the folder

#interface
@app.get("/")
def home():
    return "Hello from Flask!"
#hello

@app.get("/testing")
def test():
    return "Hello from another page!"

#create 2 more API(about and blog page)

@app.route("/about")
def about():
    me = {"name": "Mark Sanchez"}
    return json.dumps(me)

@app.route("/blog")
def blog():
    return "This is blog page"

@app.get("/version")
def version():
    version = {"name":"mouse","version":"2","build":123456}
    return json.dumps(version)

#this is what we need to read and write into the server 
products = []
@app.get("/api/products")
def get_products():
    
    return json.dumps(products)

@app.post("/api/products")
def save_products():
    #should save a new product
    product = request.get_json()
    print (product)
    #mock the save
    products.append(product)
    return json.dumps(product)

@app.get("/api/catalog")
def get_catalog():
    return json.dumps(products)

@app.post("/api/catalog")
def add_product():
    product = request.get_json()
    if not product or 'name' not in product or 'price' not in product:
        return json.dump({"error": "Product must have a name and price"}), 400
    products.append(product)
    return json.dump(product), 201



@app.get("/api/reports/total")
def get_total_value():
    total = sum(product['price'] for product in products)
    return json.dumps({"total_value": total})

@app.get("/api/products/<category>")
def get_products_by_category(category):
    filtered_products = [product for product in products if product.get('category') == category]
    return json.dumps(filtered_products)



app.run(debug=True)# apply the changes on the code, live 


#API / Endpoints
#transform JSON/ converter JSON in an object again 