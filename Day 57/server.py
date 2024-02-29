from flask import Flask,render_template
import random,requests
import datetime
GENDERIZE_ENDPOINT = 'https://api.genderize.io/'
AGIFY_ENDPOINT = 'https://api.agify.io/'

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1,10)
    current_year = datetime.date.today().year
    return render_template("./index.html",num=random_number,year=current_year)

@app.route('/guess/<name>')
def guess(name):
    params={
        'name':name
    }
    response = requests.get(GENDERIZE_ENDPOINT,params=params)
    data = response.json()
    gender = data['gender']
    response = requests.get(AGIFY_ENDPOINT,params=params)
    data = response.json()
    age = data['age']
    return render_template("./guess.html",name=name,Gender= gender,Age = age)

@app.route('/blogs')
def blog():
    blog_url = "https://api.npoint.io/82975389c85afb34e389"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("./blogs.html",posts =all_posts )

if __name__ == '__main__':
    app.run()