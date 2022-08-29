from crypt import methods
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, render_template, url_for,request,jsonify
import os
from forms import *
from flask_migrate import Migrate
import json
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

''''''
#login for admin
class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='mills', password='password'))
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
    lastname= db.Column(db.String(200), nullable=True, unique=True)
    Gender= db.Column(db.String(10), nullable=True)
    Othername = db.Column(db.Integer(),nullable = True)  
    Primary = db.Column(db.Integer(),nullable = True)  
    Other = db.Column(db.Integer(),nullable = True)  
    Kin = db.Column(db.Integer(),nullable = True)  
    Relationship = db.Column(db.Integer(),nullable = True)  
    Home = db.Column(db.Integer(),nullable = True)  
    Current = db.Column(db.Integer(),nullable = True)  
    Nationality = db.Column(db.Integer(),nullable = True)  
    Guardian = db.Column(db.Integer(),nullable = True)  
     
  
    
    def __repr__(self):
        return f"Person('{self.id}', {self.lastname}', {self.Othername})"



#yeargroup table
class YearGroup(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(200), nullable=True)
    program= db.Column(db.String(200), nullable=True)
    total_number= db.Column(db.Integer(), nullable=True)
    people_completed= db.Column(db.Integer(),nullable = True)
    people_admitted= db.Column(db.Integer(),nullable = True)

    def __repr__(self):
        return f"Course('{self.id}', {self.name}',)"
    
    
    
    
#department table
class School(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(200), nullable=True)
    name_of_school= db.Column(db.String(200), nullable=True)
    programs= db.Column(db.String(), nullable=True)
    total_number = db.Column(db.Integer(),nullable = True)
    
    def __repr__(self):
        return f"Course('{self.id}', {self.name}',)"
    
    
    
    
       
#programs table
class Program(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(200), nullable=True)
    program_name= db.Column(db.String(200), nullable=True)
    program_department= db.Column(db.String(), nullable=True)
    program_code= db.Column(db.Integer(),nullable = True)
    
    def __repr__(self):
        return f"Course('{self.id}', {self.name}',)"



#postman  
    class ProductSchema(ma.Schema):
        class Meta:
            fields = ("id","name", "age", "gender")
    product_schema = ProductSchema()
    products_schema = ProductSchema(many =True)


#routes 
#GET and POST method is working


@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/newforms')
def newforms():
    form=RegistrationForm()
    if form.validate_on_submit():
        print(form.lastname.data)
    
    return render_template("newforms.html", form=form)
    

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
        print(form.lastname.data)
        print(form.Othername.data)
        print(form.Gender.data)
        print (form.Primary.data)
        print (form.Kin.data)
        print (form.Relationship.data)
        print (form.Home.data)
        print (form.Current.data)
        print (form.Nationality.data)
        print (form.Guardian.data)
       
    
        
        new=Person(lastname=form.lastname.data, Othername=form.Othername.data, Gender=form.Gender.data, Primary=form.Primary.data,)
        
        db.session.add(new)
        db.session.commit()
        return redirect('information')
    return render_template("form.html", form=form)

@app.route('/information')
def information():
    persons=Person.query.order_by(Person.id.desc()).all()
    print(persons)
    return render_template("information.html", persons=persons)
   # print(product_schema)
 


#upgrade method 
@app.route("//<int:id>", methods=['PUT'])
def update(id):
    user=Person.query.get_or_404(id)
    if request.method== 'POST':
        print(user.name)
        user.name=request.form['name']
        try:
            db.session.commit()
            return redirect('/') 
        except:
            return"errrrror"
    else:
        return render_template('home.html', user=user)
    
    
    
#delete method
@app.route("//<int:id>",methods=['DELETE'])
def delete(id):
    delete=Person.query.get_or_404(id)
    try:
            db.session.delete(delete)
            db.session.commit()
            return redirect('/') 
    except: 
        return "errrrrorrr"
    

@app.route('/home',methods=['GET','POST'])
def home():
    persons=Person.query.all()  
    print(persons)
    return render_template('home.html',persons=persons)




#login routes for admin
#login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)
        username = request.form['username']
        password = request.form['password']
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('test'))
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/profile')
def profile():
    if not g.user:
        return redirect(url_for('login'))
    return render_template('profile.html' )


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(host='0.0.0.0', port=5000,debug=True)
    
    
