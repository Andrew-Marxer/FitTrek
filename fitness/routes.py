from flask import redirect, url_for, render_template, flash, request, session, make_response
from fitness import app, db, bcrypt
from fitness.forms import SignInForm, SignUpForm, itemForm, calorieForm, CalorieWorkoutForm
from fitness.database import User, Post, load_user, UserData
from flask_login import current_user, login_user, current_user, logout_user, login_required
from fitness import nix
from time import time
from datetime import date
import json
import sys


# Get the user database for routes
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}


# Default route
@app.route("/")
def index():
    db.create_all()
    return render_template('index copy.html')


# Protected route for user id and user consumed
@app.route("/protected")
def protected():
    return str(current_user.id)
    return str(current_user.consumed)


# Route for home page
@app.route("/home")
def home():
    return render_template('index copy.html')


# Route for about page
@app.route("/about")
def about():
    return render_template('about.html')


# Route for contact page
@app.route("/contact")
def contact():
    return render_template('contact.html')


# Route for post page
@app.route("/post")
def post():
    return render_template('post.html')


# Route for log out direction which is home page
@app.route("/logout")
@login_required
def logout():
    session.pop('fname')
    session.pop('id')
    logout_user()
    return redirect(url_for("home"))


# Route of user after they logged in
@app.route("/user")
@login_required
def user():
    total = calculate_workout()
    return render_template('user_dashboard.html', total=total)


# Route for cardio workout
@app.route("/cardio", methods=['GET', 'POST'])
@login_required
def cardio():
    form = CalorieWorkoutForm()
    if form.validate_on_submit():
        user = User.query.filter_by(id=session['id']).first()
        user_data = UserData(cardio=int(form.cardio_wo.data), user_id=session['id'])
        db.session.add(user_data)
        db.session.commit()
        return redirect(url_for('cardio'))
    total = calculate_workout()
    return render_template('cardio.html', form=form, total=total)


# Route for strength workout
@app.route("/strength")
@login_required
def strength():
    return render_template('strength.html')


# Route for clothes shopping
@app.route("/clothes")
@login_required
def clothes():
    return render_template('clothes.html')


# Route for equipment shopping
@app.route("/equipment")
@login_required
def gift():
    return render_template('equipment.html')


# Route for supplement shopping
@app.route("/supplement")
@login_required
def supplement():
    return render_template('supplement.html')


# Route for food nutrition tracking
@app.route("/tracker", methods=["GET", "POST"])
@login_required
# Tracking function form
def tracker():
    # query = nix.search().nxql(
    # filters={
    #   "nf_calories":{
    #      "lte": 500
    # }
    # },
    # fields = ["item_name","item_id","nf_calories"]
    # ).json()
    """
        form = itemForm()
        if form.validate_on_submit(): 
            searchItem = form.item.data
            query = nix.search(searchItem, results="0:1").json()
            if 'hits' in query :
                objId = query['hits'][0]['_id']
                info = nix.item(id=objId).json()
            
                filterInfo = "Name: " +str(info['item_name']) + "\ncalories: " + str(info['nf_calories']) + "\ncalories from fat: " + str(info['nf_calories_from_fat']) + "\ntotal fat(grams): " + str(info["nf_total_fat"]) + "\nsaturated fat(grams): " + str(info['nf_saturated_fat']) + "\nserving size(grams): " + str(info['nf_serving_weight_grams'])
                filterInfo = filterInfo.split('\n')
                return render_template("tracker.html", form = form, query = filterInfo)
        """
    form = calorieForm()
    if form.validate_on_submit():
        currentUser = User.query.get(id=session['id'])
        currentData = UserData.query.get(session[''])
        currentUser.consumed = int(form.consumed.data)
        currentUser.burned = int(form.burned.data)
        if (currentUser.consumed - currentUser.burned) < 0 or currentUser.calories < 0:
            currentUser.calories = 0
        else:
            currentUser.calories += (currentUser.consumed - currentUser.burned)

        db.session.commit()
        print(currentUser.consumed)

    return render_template("tracker.html", form=form)


# Sign up function for user with fields
# and store them database
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(fname=form.first_name.data, lname=form.last_name.data, email=form.email.data,
                    password=hash_password, consumed=0, burned=0, calories=0)
        db.session.add(user)
        db.session.commit()
        flash(f'Thank you for signing up with us', 'success')
        return redirect(url_for('signin'))
    return render_template('signup.html', title='Register', form=form)


# Sign up function for user with fields
# and query input information to database
# if the input match, the user will log in.
# Otherwise, error message will display
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SignInForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            session['id'] = user.id
            session['fname'] = user.fname
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('signin.html', form=form)


@login_required
def calculate_workout():
    get_all = UserData.query.filter_by(user_id=session['id']).all()
    total_cardio = 0
    total_strength = 0
    for item in get_all:
        if item.cardio is not None:
            total_cardio = total_cardio + item.cardio
        if item.strength is not None:
            total_strength = total_strength + item.strength
    total = total_strength + total_cardio
    return total
