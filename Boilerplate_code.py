#Importing flask module in the project
from flask import Flask, render_template

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class 
@app.route("/")

#‘/’ URL is bound with first_flask function.
def first_flask():

    return "This is my first flask program"

#run the application on local server
@app.route("/Hello")

def second_flask():
    return "This is my second flask program"

@app.route("/third")

def html_flask():
    return render_template('index.html', variable = 'flask')

app.run(debug= True)
