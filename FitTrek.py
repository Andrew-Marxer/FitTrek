from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)



@app.route("/")
def index():
    return render_template('index copy.html')

@app.route("/home")
def home():
    return render_template('index copy.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/post")
def post():
    return render_template('post.html')

@app.route("/signin")
def login():
    return render_template('signin.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')


if __name__ == "__main__":
    app.run(debug=True)