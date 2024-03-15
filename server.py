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


app.run(debug=True)# apply the changes on the code, live 


#API / Endpoints
#transform JSON/ converter JSON in an object again 