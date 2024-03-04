from flask import Flask,render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("./index.html")

@app.route('/login',methods=['POST'])
def receive_data():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['pws']
        return render_template("./login.html",uname = username,password = password)

if __name__ == '__main__':
    app.run()