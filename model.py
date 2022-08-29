from app import db


#complaint form(model)
class Person(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    surname= db.Column(db.String(100), nullable=True)
    firstname= db.Column(db.String(100), nullable=True)
    others = db.Column(db.String(100),nullable = True)  
    registration_no= db.Column(db.Integer(),nullable = True)
    old_registration_no= db.Column(db.Integer(),nullable = True)
    program= db.Column(db.String(),nullable = True)
    level= db.Column(db.Integer(),nullable = True)
    DOB=db.Column(db.date(),)
    telephone_no= db.Column(db.Integer(),nullable = True)
    
    def __repr__(self):
        return f"('Peron{self.registration_no}', {self.program}',)"

#department  complaint   
class Complaint(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    course_code= db.Column(db.Integer(100), nullable=True)
    course_titles= db.Column(db.String(100), nullable=True)
    name_of_faculty= db.Column(db.String(100),nullable = True)  
    name_of_department= db.Column(db.String(),nullable = True)
    name_of_lecturer= db.Column(db.String(),nullable = True)
    year= db.Column(db.Integer(),nullable = True)
    semester= db.Column(db.String(),nullable = True)
    paper_session = db.Column(db.String(),nullable = True)
    grade = db.Column(db.String(),nullable = True)
    nature_of_complaint = db.Column(db.String(),nullable = True)
    
    def __repr__(self):
        return f"('Complaint{self.id})"
#complaint form(model/ end)
    
    