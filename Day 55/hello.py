from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1 style = "text-align:center">Hello world</h1>\
    <p>Harsh</p>\
    <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjdkNGo2MmJiOGY1cnk5bnJjbHkyNjZldGkzeDJua2hrbTNsMjZxYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/V3Z76ctCO3jG0/giphy.gif",width=200>'

def makeBold(function):
    def innerFunc():
        return "<b>"+function()+"</b>"
    return innerFunc

def makeEmphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def makeUnderlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route('/bye')

@makeBold
@makeEmphasis
@makeUnderlined
def bye():
    return "Bye"

@app.route('/<name>/<int:number>')
def greet(name,number):
    return f"<h1>Hello there {name} who is {number} years old!</h1>"

print(__name__)

if app.name == '__main__':
    app.run(debug=True)