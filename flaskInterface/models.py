from datetime import datetime

from flaskInterface import db  ,login_manager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin



@login_manager.user_loader
def load_user(user_id):
    
    return  User.query.get(int(user_id))




class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email =  db.Column(db.String(100),unique=True,nullable=False)
    password =  db.Column(db.String(60), nullable=False)
    userTask  = db.relationship('TaskProcessor', backref='user')

    def __str__(self):
        return f"User-{self.username} "

class Domain(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32),nullable=False, unique=True)
    description =  db.Column(db.Text, nullable=True)

    def __repr__(self):

        return self.title

        
class TaskProcessor(db.Model):
    id =  db.Column(db.Integer, primary_key=True)
    Ms_Name =  db.Column(db.String(62),nullable=False)
    FField =  db.Column(db.Text , nullable=False)
    desired_output = db.Column(db.String(64))
    Namespace = db.Column(db.String(120))
    purpose = db.Column(db.Text)
    domain =  db.Column(db.String(64), db.ForeignKey('domain.title'))
    created_by =  db.Column(db.String, db.ForeignKey('user.username'))
    
    



   

    def __repr__(self):
        return f'Task:-->{self.title}'

class ServiceRegister(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Namespace  = db.Column(db.String(150), nullable=False)
    Ms_name = db.Column(db.String(150), nullable=False)
    Description =  db.Column(db.String(150))
    Ms_type = db.Column(db.String(150), ) 
    Dependencies =  db.Column(db.String(150))
    Framework=   db.Column(db.String(160))
    GPU =  db.Column(db.String(7), default=False, nullable=False )
    Pipeline =  db.Column(db.String(60),nullable=True)
    Model_format =  db.Column(db.String(60))
    Invoke_uri =  db.Column(db.String(60))
    Input_sp= db.Column(db.String(60), )
    Output_sp =  db.Column(db.String(70))
    Contributor  = db.Column(db.String(60))
    License  =  db.Column(db.String(60))
    Service_category =  db.Column(db.String(60))

def init_db():
    db.create_all()


init_db()




'''


     {{form.fileInput.label(class='form-label fw-bolder')}}
                {{form.fileInput(class='form-control')}}
'''

