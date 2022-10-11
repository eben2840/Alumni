
import os

import secrets
import urllib.request, urllib.parse
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, render_template, url_for,request,jsonify,get_flashed_messages
from flask_migrate import Migrate
import json
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField, SelectField, IntegerField,PasswordField, SearchField
from flask_login import login_required,login_user,logout_user,current_user,UserMixin, LoginManager
from flask_marshmallow import Marshmallow
from flask import(
Flask,g,redirect,render_template,request,session,url_for,flash,jsonify
)
from flask_cors import CORS



app=Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] =" thisismysecretkey"
app.config['UPLOADED_PHOTOS_DEST'] ='uploads'

# photos=UploadSet('photos', IMAGES)
# configure_uploads(app, photos)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)



login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"
migrate = Migrate(app, db)
from forms import *

@login_manager.user_loader
def load_user(user_id):
    return Person.query.get(int(user_id))


''''
#login for admin
class User:
    username = StringField('username', validators=[DataRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[DataRequired(), Length(min=8, max=80)])
    submit = SubmitField('Login')
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
'''

#DATABASE MODEL
#person table
class Person(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(200), nullable=True)
    yearCompleted= db.Column(db.String(200), nullable=True)
    nationality= db.Column(db.String(200), nullable=True)
    contact= db.Column(db.Integer(), nullable=True)
    email= db.Column(db.String(200), nullable=True)
    faculty= db.Column(db.String(200), nullable=True)
    hallofresidence= db.Column(db.String(200), nullable=True)
    password= db.Column(db.String(20))
    school= db.Column(db.String(20))
    email= db.Column(db.String(20), nullable=True)
    phone= db.Column(db.String(10), nullable=True )
    indexnumber=db.Column(db.String())
    password=db.Column(db.String)
    gender= db.Column(db.String()    )
    department= db.Column(db.String()    )
    program= db.Column(db.String()   )
    telephone= db.Column(db.String()   )
    admitted= db.Column(db.Integer()  )
    address= db.Column(db.String()   )
    work= db.Column(db.String()  )
    guardian= db.Column(db.String()  )
    kin= db.Column(db.String()   )
    relationship= db.Column(db.String()  )
    marital= db.Column(db.String()   )
    health= db.Column(db.String()    )
    form=db.Column(db.String())
    extra= db.Column(db.String()     )
    image_file = db.Column(db.String(20))
    
    
   
    def __repr__(self):
        return f"Person('{self.id}', {self.name}', {self.yearCompleted})"

class alumni(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    email= db.Column(db.String(20) )
    name= db.Column(db.String(200) )
    password= db.Column(db.String(200) )
    email= db.Column(db.String(20) )
    indexnumber= db.Column(db.String(10)  )
    telephone= db.Column(db.String(10)  )
    
  
    
    
class User(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    fullname= db.Column(db.String()  )
    indexnumber= db.Column(db.Integer())
    gender= db.Column(db.String()    )
    school= db.Column(db.String()    )
    department= db.Column(db.String()    )
    program= db.Column(db.String()   )
    completed= db.Column(db.Integer()     )
    admitted= db.Column(db.Integer()  )
    email= db.Column(db.String()     )
    telephone= db.Column(db.String()     )
    hall= db.Column(db.String()  )
    nationality= db.Column(db.String()   )
    address= db.Column(db.String()   )
    work= db.Column(db.String()  )
    guardian= db.Column(db.String()  )
    kin= db.Column(db.String()   )
    relationship= db.Column(db.String()  )
    marital= db.Column(db.String()   )
    health= db.Column(db.String()    )
    extra= db.Column(db.String()     )
    image_file = db.Column(db.String(20))
    
@app.route('/dashboard')
@login_required
def dashboard():
    if current_user == None:
        flash("Welcome to the CentralAlumina " + current_user.email, "Success")
        flash(f"There was a problem")
    return render_template('dashboard.html', title='dashboard')




@app.route('/addalumni', methods=['GET', 'POST'])
@login_required
def addalumni():
    form=Adduser()
    if form.validate_on_submit():
  
            new=User(fullname=form.fullname.data,
                 indexnumber=form.indexnumber.data,
                   gender=form.gender.data, 
                    school=form.school.data,
                    department=form.department.data,
                   completed=form.completed.data,
                   admitted=form.admitted.data,
                   email=form.email.data,  
                   telephone=form.telephone.data,  
                   hall=form.hall.data,  
                   nationality=form.nationality.data,  
                   address=form.address.data,  
                   work=form.work.data,  
                   guardian=form.guardian.data,  
                  marital=form.marital.data,
                  extra=form.extra.data,    
               image_file=form.image_file.data
                  )
       
            db.session.add(new)
            db.session.commit()
            flash("New Alumni Added", "success")
            return redirect('list')
    print(form.errors)
    return render_template("addAlumni.html", form=form, title='addalumni')


@app.route('/department', methods=['GET', 'POST'])
@login_required
def department():
    return render_template('department.html')


@app.route('/current', methods=['GET', 'POST'])
@login_required
def current():
    return render_template('current.html')



@app.route('/newreport')

def upload_image():
    return render_template('newreport.html')


@app.route('/')
def index():    
    return render_template('index.html')


@app.route('/userprofile', methods=['GET', 'POST'])
def userprofile():
    form=RegistrationForm()
    if form.validate_on_submit():
  
            new=Person(name=form.name.data,
                 indexnumber=form.indexnumber.data,
                   gender=form.gender.data, 
                    school=form.school.data,
                    department=form.department.data,
                   yearCompleted=form.yearCompleted.data,
                   admitted=form.admitted.data,
                   email=form.email.data,  
                   telephone=form.telephone.data,  
                   hallofresidence=form.hallofresidence.data,  
                   nationality=form.nationality.data,  
                   address=form.address.data,  
                   work=form.work.data,  
                   guardian=form.guardian.data,  
                  marital=form.marital.data,
                  extra=form.extra.data,    
            
                  )
       
            db.session.add(new)
            db.session.commit()
            flash("New Alumni Added", "success")
            return redirect('information')
    print(form.errors)
    return render_template("userprofile.html", form=form, title='addalumni')
 


@app.context_processor
def base():
    form=Search()
    return dict(form=form)


@app.route('/search', methods=[ 'POST'])
def search():
    form= Search()
    if request.method == 'POST': 
        posts =User.query
        if form.validate_on_submit():
            postsearched=form.searched.data
            posts =posts.filter(User.fullname.like('%'+ postsearched + '%') )
            posts =posts.order_by(User.indexnumber).all() 
            flash("You searched for "+ postsearched, "success")  
            print(posts)   
    return render_template("search.html", form=form, searched =postsearched, posts=posts)



@app.route('/newreport', methods=[ 'POST'])
@login_required
def newreport():
    form= Adsearch()
    if request.method == 'POST': 
        posts =User.query
        if form.validate_on_submit():
            postsearched=form.searched.data
            # posts =posts.filter(User.fullname.like('%'+ postsearched + '%') )
            #posts =posts.filter(User.indexnumber.like('%'+ postsearched + '%') )
            posts =posts.filter(User.completed.like('%'+ postsearched + '%') )
            # posts =posts.filter(User.department.like('%'+ postsearched + '%') )
            posts =posts.order_by(User.indexnumber).all() 
            flash("You searched for "+ postsearched, "success")  
            print(posts)   
    return render_template("newreport.html", form=form, searched =postsearched, posts=posts)

#search for user
@app.route('/usersearch', methods=[ 'POST'])
def usersearch():
    form= UserSearch()
    if request.method == 'POST': 
        posts =User.query
        if form.validate_on_submit():
            postsearched=form.searched.data
            posts =posts.filter(User.fullname.like('%'+ postsearched + '%') )
            posts =posts.order_by(User.indexnumber).all() 
            flash("You searched for "+ postsearched, "success")  
            print(posts)   
    return render_template("usersearch.html", form=form, searched =postsearched, posts=posts, header="Year Group", smalltitle="Central Alumni Platform", name="", numberofentries="16 entries")



@app.route('/year', methods=['GET', 'POST'])
@login_required
def year():
    return render_template('year.html', title='year')


@app.route('/list/<int:userid>', methods=['GET', 'POST'])
@login_required
def list(userid):
    print("Fetching one")
    profile=User.query.get_or_404(userid)
    print(current_user)
    return render_template("profileid.html",current_user=current_user, profile=profile, title="list")
 
 
 
@app.route('/list', methods=['GET', 'POST'])
@login_required
def lists():
    print("Fetching all")
    users=User.query.order_by(User.id.desc()).all()
    print(users)
    print(current_user)
    return render_template("list.html", users=users, current_user=current_user, title="list")
 


@app.route('/newschools', methods=['GET', 'POST'])
def newschools():
    return render_template('newschools.html', title="newschools")


@app.route('/logout')
@login_required
def logout():
    if current_user:
        print(current_user.email)
        logout_user()
    else:
        print("Well that didnt work")
    flash('You have been logged out.','danger')
    return redirect(url_for("login"))


@app.route('/userlogout')
@login_required
def userlogout():
    if current_user:
        logout_user()
        print(current_user.email)
    else:
        print("Well that didnt work")
    flash('You have been logged out.','danger')
    return redirect(url_for("userlogin"))

@app.route('/report')
@login_required
def report():
    return render_template('report.html')








@app.route('/newforms')
@login_required
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
@login_required
def members():
    persons=Person.query.all()
    return render_template('members.html', persons=persons)

@app.route('/schools')
@login_required
def schools():
    return render_template('schools.html')

@app.route('/form', methods=['POST', 'GET'])
def form():
    form=RegistrationForm()
    if form.validate_on_submit():
       
        new=Person(name=form.name.data, yearCompleted=form.yearCompleted.data,
                   nationality=form.nationality.data, 
                   contact=form.contact.data, email=form.email.data,faculty=form.faculty.data,
                   hallofresidence=form.hallofresidence.data, password=form.password.data)
        db.session.add(new)
        db.session.commit()
        return redirect('information')
       
    flash("Added a New Alumni", "success")
    print(form.errors)
    return render_template("form.html", form=form)

@app.route('/information')
@login_required
def information():
    persons=Person.query.order_by(Person.id.desc()).all()
    print(persons)
    return render_template("information.html", persons=persons)
 



#CRUD(update and delete routes)
@app.route("/update/<int:id>", methods=['POST', 'GET'])
def update(id):
    form=Adduser()
    user=User.query.get_or_404(id)
    if request.method== 'GET':
        form.fullname.data = user.fullname
        form.indexnumber.data = user.indexnumber
        form.gender.data = user.gender
        form.school.data = user.school
        form.department.data = user.department
        form.completed.data = user.completed
        form.admitted.data = user.admitted
        form.email.data = user.email   
        form.telephone.data = user.telephone  
        form.hall.data = user.hall  
        form.nationality.data = user.nationality   
        form.address.data = user.address  
        form.work.data = user.work 
        form.guardian.data = user.guardian   
        form.marital.data = user.marital   
        form.extra.data = user.extra  
        form.image_file.data = user.image_file 
    if request.method== 'POST':
        new=User(fullname=form.fullname.data,
                 indexnumber=form.indexnumber.data,
                   gender=form.gender.data, 
                    school=form.school.data,
                    department=form.department.data,
                   completed=form.completed.data,
                   admitted=form.admitted.data,
                   email=form.email.data,  
                   telephone=form.telephone.data,  
                   hall=form.hall.data,  
                   nationality=form.nationality.data,  
                   address=form.address.data,  
                   work=form.work.data,  
                   guardian=form.guardian.data,  
                  marital=form.marital.data,
                  extra=form.extra.data,    
               image_file=form.image_file.data
                  )
        try:    
            db.session.add(new)
            db.session.commit()
            return redirect(url_for('list')) 
        except:
            return render_template("dashboard.html")
    return render_template("addAlumni.html", form=form)
    
    
#CRUD(update and delete routes)
@app.route("/updateuser/<int:id>", methods=['POST', 'GET'])
def updateuser(id):
    form=RegistrationForm()
    user=Person.query.get_or_404(id)
    if request.method== 'GET':
        form.name.data = user.name
        form.indexnumber.data = user.indexnumber
        form.gender.data = user.gender
        form.school.data = user.school
        form.department.data = user.department
        form.yearCompleted.data = user.yearCompleted
        form.admitted.data = user.admitted
        form.email.data = user.email   
        form.telephone.data = user.telephone  
        form.hallofresidence.data = user.hallofresidence  
        form.nationality.data = user.nationality   
        form.address.data = user.address  
        form.work.data = user.work 
        form.guardian.data = user.guardian   
        form.marital.data = user.marital   
        form.extra.data = user.extra  
        form.image_file.data = user.image_file 
    if request.method== 'POST':
        new=Person(name=form.name.data,
                 indexnumber=form.indexnumber.data,
                   gender=form.gender.data, 
                    school=form.school.data,
                    department=form.department.data,
                   yearCompleted=form.yearCompleted.data,
                   admitted=form.admitted.data,
                   email=form.email.data,  
                   telephone=form.telephone.data,  
                   hallofresidence=form.hallofresidence.data,  
                   nationality=form.nationality.data,  
                   address=form.address.data,  
                   work=form.work.data,  
                   guardian=form.guardian.data,  
                  marital=form.marital.data,
                  extra=form.extra.data,    
               image_file=form.image_file.data
                  )
        try:    
            db.session.add(new)
            db.session.commit()
            return redirect(url_for('information')) 
        except:
            return "errror"
    return render_template("userprofile.html", form=form)
    
    
#delete route
@app.route("/delete/<int:id>")
def delete(id):
    delete=User.query.get_or_404(id)
    try:
            db.session.delete(delete)
            db.session.commit()
            return redirect(url_for('list')) 
    except: 
        return "errrrrorrr"
    



''''
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

        return redirect(url_for('login'))
    else:
        flash("wrong password-try again!" "danger")
    return render_template('login.html')
'''

@app.route('/login', methods=['POST','GET'])
def login():
    form = LoginForm()
    print ('try')
    print(form.email.data)
    print(form.password.data)
    
    if form.validate_on_submit():
        print("form Validated successfully")
        user = Person.query.filter_by(email = form.email.data).first()
        print("user:" + user.email + "found")
      
        print(user.password)
        if user and form.password.data == user.password:
            print(user.email + "validored successfully")
            if user == None:
                flash(f"There was a problem")   
            login_user(user)
            flash (f' ' + user.email + ',Welcome Admin ' ,'success')
            return redirect(url_for('dashboard'))
            # next = request.args.get('next')
        else:
            flash (f'Wrong Password ', 'success')
   
    return render_template('login.html', form=form)
 

#signup route
@app.route('/signup', methods=['POST','GET'])

def signup():
    form = Registration()
    print(form.phone.data)
    print(form.email.data)
    print(form.name.data)
    
    if request.method == "POST": 
        if form.validate_on_submit():
            print('Success')
            user =Person(password="central@123", email=form.email.data, phone=form.phone.data, name=form.name.data)
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)
            print(current_user)
         
            return redirect(url_for('login'))
        else:
            print(form.errors)
            
    return render_template('signup.html', form=form)

#user land area
@app.route('/userlanding')
def userlanding():
    return render_template('userlanding.html')

@app.route('/usersignup', methods=['POST','GET'])
def usersignup():
    form = Registration()
    print(form.indexnumber.data)
    print(form.email.data)
    print(form.name.data)
    
    if request.method == "POST": 
        if form.validate_on_submit():
            print('Success')
            user =Person(password="central@123", email=form.email.data, indexnumber=form.indexnumber.data, name=form.name.data)
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)
            print(current_user)
         
            return redirect(url_for('ulogin'))
        else:
            print(form.errors)
            
    return render_template('usersignup.html', form=form)
   

@app.route('/userlogin', methods=['POST','GET'])
def ulogin():
    form = LoginForm()
    print ('try')
    print(form.email.data)
    print(form.password.data)
    
    if form.validate_on_submit():
        print("form Validated successfully")
        user = Person.query.filter_by(email = form.email.data).first()
        print("user:" + user.email + "found")
        print(user.password)
        if user and form.password.data == user.password:
            print(user.email + "validored successfully")
            login_user(user)
            flash ('Welcome, Finish Setting up your profile ' ,'success')
            return redirect(url_for('useryeargroup'))
            # next = request.args.get('next')
        else:
            flash (f'Wrong Password', 'success')
    return render_template('userlogin.html', form=form)

   





@app.route('/useryeargroup', methods=['GET', 'POST'])
@login_required
def useryeargroup():  
    
    return render_template("useryeargroup.html", header="Year Group", smalltitle="Central Alumni Platform", name="", numberofentries="16 entries")
 


@app.route('/usernewform')
@login_required
def usernewform():
    return render_template('usernewform.html', header="Schools / Faculty", smalltitle="2021", name="", numberofentries="16 entries")


@app.route('/userschool')
@login_required
def userschool():
    return render_template('userschool.html', header="Department", smalltitle="2021", name="- CCSITA", numberofentries="16 entries")


# @app.route('/userdisplay')
# @login_required
# def userdisplay(userid):
#     profile=User.query.get_or_404(userid)
#     print(current_user)
#     return render_template("userdisplay.html",current_user=current_user, profile=profile)
 
 
@app.route('/userdisplay/<int:userid>', methods=['GET', 'POST'])
@login_required
def userdisplay(userid):
  
    profile=User.query.get_or_404(userid)
    print(current_user)
    return render_template("userdisplay.html",current_user=current_user, profile=profile, title="list")
 
   


@app.route('/userbase')
@login_required
def userbase():
    print("Fetching all")
    users=User.query.order_by(User.id.desc()).all()
    print(users)
    print(current_user)
    return render_template("userbase.html", users=users, current_user=current_user, header="Information Technology", smalltitle="2021", name="- CCSITA", numberofentries="16 entries")
 

  


@app.route('/userinformation/<int:userid>', methods=['GET', 'POST'])
@login_required
def userinformation(userid):
    profile=User.query.get_or_404(userid)
    print(current_user)
    return render_template("userinformation.html",current_user=current_user, profile=profile, title="list")
 
   
#ending user



if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(host='0.0.0.0', port=4000, debug=True)
    
    
