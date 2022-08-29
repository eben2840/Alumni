from sqlite3 import ProgrammingError
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField, SelectField
from flask_wtf import FlaskForm

class RegistrationForm(FlaskForm):
    lastname = StringField('Lastname')
    Othername= StringField('Othername')
    Gender = StringField('Gender')
    Other = StringField('Other')
    Primary = StringField('Primary')
    Kin = StringField('Kin')
    Relationship = StringField('Relationship')
    Home = StringField('Home')
    Current  = StringField('Current ')
    Nationality = StringField('Nationality')
    Guardian = StringField('Guardian')
    School = StringField('School')
    Year = StringField('Year')
    Marital = StringField('Marital')
    Health = StringField('Health')
    Extra  = StringField('Extra ')
    
    
    Program = SelectField('programs', choices=[("one", "one"),("two", "two"),("three", "three")])
    submit =SubmitField('submit')
    
    
    