from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField, SelectField, IntegerField,PasswordField, SearchField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
# from app import Person


class RegistrationForm(FlaskForm):
    id = IntegerField('id', validators=[(DataRequired())])
    name = StringField('name', validators=[(DataRequired())])
    yearCompleted= SelectField('yearCompleted', choices=[(2021,2021)])
    nationality = StringField('nationality',validators=[DataRequired()] )
    contact= StringField('contact',validators=[ DataRequired(), Length(min=10, max=10, message="Your number shouldn't be less than 10")])
    email = StringField('email',validators=[(DataRequired() )])
    faculty = SelectField('faculty',  choices=[('Faculty/School','Faculty/School'),('Joy Otabil', 'Joy Otabil'), ('Faith','Faith'), ('Freedom','Freedom'), ('Kathryl Kuhlman ', 'Kathryl Kuhlman '), ('Justice','Justice'), ('Billy Graham','Billy Graham'),('Billy Graham','Billy Graham'),  ('Chancellor', 'Chancellor'),('Integerity','Integerity'), ], default=None )
    hallofresidence = SelectField('hallofresidence',  choices=[('Halls','Halls'),('Joy Otabil', 'Joy Otabil'), ('Faith','Faith'), ('Freedom','Freedom'), ('Kathryl Kuhlman ', 'Kathryl Kuhlman '), ('Justice','Justice'), ('Billy Graham','Billy Graham'),('Billy Graham','Billy Graham'),  ('Chancellor', 'Chancellor'),('Integerity','Integerity'), ], default=None )
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Register')

class Adduser(FlaskForm):
    fullname = StringField('fullname')
    indexnumber= StringField('indexnumbe')
    gender= SelectField('gender', choices=[('Gender','Gender'),('Male', 'Male'), ('Female','Female') ], default=None )
    school=SelectField('school',choices=[('Faculty/School','Faculty/School'),('Joy Otabil', 'Joy Otabil'), ('Faith','Faith'), ('Freedom','Freedom'), ('Kathryl Kuhlman ', 'Kathryl Kuhlman '), ('Justice','Justice'), ('Billy Graham','Billy Graham'),('Billy Graham','Billy Graham'),  ('Chancellor', 'Chancellor'),('Integerity','Integerity'), ], default=None )
    department=SelectField('department',choices=[('Faculty/School','Faculty/School'),('Joy Otabil', 'Joy Otabil'), ('Faith','Faith'), ('Freedom','Freedom'), ('Kathryl Kuhlman ', 'Kathryl Kuhlman '), ('Justice','Justice'), ('Billy Graham','Billy Graham'),('Billy Graham','Billy Graham'),  ('Chancellor', 'Chancellor'),('Integerity','Integerity'), ], default=None )
    program= SelectField('program',choices=[('Faculty/School','Faculty/School'),('Joy Otabil', 'Joy Otabil'), ('Faith','Faith'), ('Freedom','Freedom'), ('Kathryl Kuhlman ', 'Kathryl Kuhlman '), ('Justice','Justice'), ('Billy Graham','Billy Graham'),('Billy Graham','Billy Graham'),  ('Chancellor', 'Chancellor'),('Integerity','Integerity'), ], default=None )
    completed= SelectField('completed',choices=[(2021,2021), (2022,2022)])
    admitted=SelectField('admitted',choices=[(2021,2021), (2022,2022)])
    email= StringField('email')
    telephone= StringField('telephone')
    hall= SelectField('hall', choices=[('Faculty/School','Faculty/School'),('Joy Otabil', 'Joy Otabil'), ('Faith','Faith'), ('Freedom','Freedom'), ('Kathryl Kuhlman ', 'Kathryl Kuhlman '), ('Justice','Justice'), ('Billy Graham','Billy Graham'),('Billy Graham','Billy Graham'),  ('Chancellor', 'Chancellor'),('Integerity','Integerity'), ], default=None )
    nationality= SelectField('nationality',choices=[('Faculty/School','Faculty/School'),('Joy Otabil', 'Joy Otabil'), ('Faith','Faith'), ('Freedom','Freedom'), ('Kathryl Kuhlman ', 'Kathryl Kuhlman '), ('Justice','Justice'), ('Billy Graham','Billy Graham'),('Billy Graham','Billy Graham'),  ('Chancellor', 'Chancellor'),('Integerity','Integerity'), ], default=None )
    address= StringField('address')
    work= StringField('work')
    guardian= StringField('guardian')
    marital= SelectField('Marital',  choices=[('Marital Status','Marital Status'),('Married', 'Married'), ('Divored','divored') ], default=None )
    picture = FileField('Add a picture', validators=[ FileAllowed(['jpg', 'png','jpeg'])])
    extra= StringField('extra')
    submit = SubmitField('Register')
    image_file = FileField('image_file', validators=[FileAllowed(['jpg', 'png'])])
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
 
class Registration(FlaskForm):
    #indexNumber= StringField('indexNumber', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    
    submit = SubmitField('SignUp')  
    
    # el4 = SelectField('el4', default='None', choices=[(user.lastname, user.lastname) for user in Person.query.all()])
  
    
    #Program = SelectField('programs', choices=[("one", "one"),("two", "two"),("three", "three")])
    submit =SubmitField('submit')
    
# create a search form
class Search(FlaskForm):
    searched = StringField('Searched', validators=[DataRequired()])
    submit = SubmitField('Search') 
    
    
    
class Alumni(FlaskForm):
    email= StringField('email', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    submit = SubmitField('SignUp')  
    

class AlumniSignin(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    indexnumber = StringField('indexnumber', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    
    submit = SubmitField('SignUp')  
    