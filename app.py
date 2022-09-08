from telnetlib import LOGOUT
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, render_template, url_for,request,jsonify,get_flashed_messages
from flask_migrate import Migrate
import json
from flask_login import login_user,logout_user,current_user,UserMixin, LoginManager
from flask_marshmallow import Marshmallow
from flask import(
Flask,g,redirect,render_template,request,session,url_for,flash,jsonify
)
from flask_cors import CORS

app=Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] =" thisismysecretkey"


db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

from forms import *



login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



#login for admin
class User:
    username = StringField('username', validators=[DataRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[DataRequired(), Length(min=8, max=80)])

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='admin', password='central'))
users.append(User(id=2, username='likem', password='likem'))
users.append(User(id=3, username='john', password='some'))



@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user


#DATABASE MODEL
#person table
class Person(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(200), nullable=True, unique=True)
    yearCompleted= db.Column(db.String(200), nullable=True, unique=True)
    nationality= db.Column(db.String(200), nullable=True, unique=True)
    contact= db.Column(db.Integer(), nullable=True, unique=True)
    email= db.Column(db.String(200), nullable=True, unique=True)
    faculty= db.Column(db.String(200), nullable=True, unique=True)
    hallofresidence= db.Column(db.String(200), nullable=True, unique=True)
    
    def __repr__(self):
        return f"Person('{self.id}', {self.name}', {self.yearCompleted})"



#routes 
@app.route('/test')
def test():
    flash("Welcome to the CentralAlumina", "success")
    return render_template('test.html')

@app.route('/base')
def base():
    
    return render_template('base.html')

@app.route('/logout')
def logout():
     return (url_for("login.html"))
 
@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/newforms')
def newforms():
    form=RegistrationForm()
    if form.validate_on_submit():
        print(form.lastname.data)
    
    return render_template("newforms.html", form=form)
   

@app.route('/home',methods=['GET','POST'])
def home():
    persons=Person.query.all()  
    print(persons)
    return render_template('home.html',persons=persons)

@app.route('/members')
def members():
    persons=Person.query.all()
    return render_template('members.html', persons=persons)

@app.route('/schools')
def schools():
    return render_template('schools.html')

@app.route('/form', methods=['POST', 'GET'])
def form():
    form=RegistrationForm()
    if form.validate_on_submit():
       
        new=Person(name=form.name.data, yearCompleted=form.yearCompleted.data,
                   nationality=form.nationality.data, 
                   contact=form.contact.data, email=form.email.data,faculty=form.faculty.data,
                   hallofresidence=form.hallofresidence.data)
        db.session.add(new)
        db.session.commit()
        return redirect('information')
       
    flash("please fill this form", "success")
    print(form.errors)
    return render_template("form.html", form=form)

@app.route('/information')
def information():
    persons=Person.query.order_by(Person.id.desc()).all()
    print(persons)
    return render_template("information.html", persons=persons)
 
 


#CRUD(update and delete routes)
@app.route("/update/<int:id>")
def update(id):
    form=RegistrationForm()
    user=Person.query.get_or_404(id)
    if request.method== 'GET':
        form.name.data = user.name
        form.yearCompleted.data = user.yearCompleted
        form.nationality.data = user.nationality
        form.contact.data = user.contact
        form.email.data = user.email
        form.faculty.data = user.faculty
        form.hallofresidence.data = user.hallofresidence    
    if request.method== 'POST':
        new=Person(id=form.id.data, name=form.name.data, 
                   yearCompleted=form.yearCompleted.data, 
                   nationality=form.nationality.data,
                   contact=form.contact.data,email=form.email.data,faculty=form.faculty.data,
                   hallofresidence=form.hallofresidence.data)
        try:    
            db.session.add(new)
            db.session.commit()
            return redirect(url_for('information')) 
        except:
            return"errrrror"
    return render_template("form.html", form=form)
    
    
#delete route
@app.route("/delete/<int:id>")
def delete(id):
    delete=Person.query.get_or_404(id)
    try:
            db.session.delete(delete)
            db.session.commit()
            return redirect(url_for('information')) 
    except: 
        return "errrrrorrr"
    




#login routes for admin
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)
        username = request.form['username']
        password = request.form['password']
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            return redirect(url_for('test'))
        else:
            flash("wrong password-try again!")

        return redirect(url_for('login'))
    else:
        flash("wrong password-try again!" "danger")
    return render_template('login.html')
if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(host='0.0.0.0', port=3000,debug=True)
    
    
