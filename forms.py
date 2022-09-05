from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField, SelectField
from flask_wtf import FlaskForm
from app import Person


class RegistrationForm(FlaskForm):
    lastname = StringField('Lastname')
    Othername= StringField('Othername')
    Gender = StringField('Gender')
    Primary = StringField('Primary')
    
    Other = StringField('Other')
    Kin = StringField('Kin')
    Relationship = StringField('Relationship')
    Home = StringField('Home')
    Current  = StringField('Current ')
    Nationality = StringField('Nationality')
  
    
    Marital = StringField('Marital')
    Health = StringField('Health')
    Extra  = StringField('Extra ')
    
    
    el4 = SelectField('el4', default='None', choices=[(user.lastname, user.lastname) for user in Person.query.all()])
  
    
    Program = SelectField('programs', choices=[("one", "one"),("two", "two"),("three", "three")])
    submit =SubmitField('submit')
    
    
    