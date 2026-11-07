from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<name>')
def guess(name):
    # Added 'f' before the quotes to enable string formatting
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data['gender']

    # Added 'f' before the quotes here as well
    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data['age']
    return render_template('guess.html', person_name=name, gender=gender, age=age)

@app.route('/blog')
def get_blog():
    blog_url = "https://api.npoint.io/e4dcc2a41ee5e151f6fd"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)

if __name__ == '__main__':
    app.run(debug=True)



























