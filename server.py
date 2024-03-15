from flask import Flask

app = Flask(__name__)# This is the name of the folder

#interface
app.get("/")
def home():
    return "Hello from Flask!"


app.run(debug=True)# apply the changes on the code, live 