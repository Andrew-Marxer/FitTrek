from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)



@app.route("/")
def index():
    return render_template('index.html')

@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/post")
def post():
    return render_template('post.html')



"""
@app.route("/")
def contact():
    return render_template("contact.html")

@app.route("/")
def about():
    return render_template("about.html")

@app.route("/")
def post():
    return render_template("post.html")
"""

if __name__ == "__main__":
    app.run(debug=True)