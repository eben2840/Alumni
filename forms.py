from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField, SelectField, IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
# from app import Person


class RegistrationForm(FlaskForm):
    id = IntegerField('id', validators=[(DataRequired())])
    name = StringField('name', validators=[(DataRequired() )])
    yearCompleted= SelectField('yearCompleted', choices=[(2021,2021)])
    nationality = StringField('nationality',validators=[DataRequired()] )
    contact= StringField('contact',validators=[ DataRequired(), Length(min=10, max=15, message="Your number shouldn't be less than 10")])
    
    email = StringField('email',validators=[(DataRequired() )])
    faculty =SelectField('faculty', choices=[(2021,2021)])
    hallofresidence = SelectField('hallofresidence', choices=[(2021,2021)])
    
    
    
    # el4 = SelectField('el4', default='None', choices=[(user.lastname, user.lastname) for user in Person.query.all()])
  
    
    #Program = SelectField('programs', choices=[("one", "one"),("two", "two"),("three", "three")])
    submit =SubmitField('submit')
    
    
    