from flask import Flask,render_template
import requests

posts = requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()

app = Flask(__name__)

@app.route('/')
def home():
    pre = '../static/'
    return render_template("./index.html",pre = pre)

@app.route("/about")
def about():
    return render_template("./about.html")

@app.route("/samplepost")
def sample_post():
    return render_template('./post.html',post_list = posts)

@app.route("/contact")
def contact():
    return render_template('./contact.html')
    


if __name__ == '__main__':
    app.run()