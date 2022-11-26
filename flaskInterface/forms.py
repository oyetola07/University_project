from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField , BooleanField, SelectField, IntegerField
from wtforms.validators import DataRequired,EqualTo,Length,Email ,ValidationError
from flaskInterface.models import User,Domain,TaskProcessor
from flask_login import  current_user
from flask_wtf.file  import FileField, FileAllowed
from wtforms.widgets import TextArea
from wtforms_sqlalchemy.fields import QuerySelectField
from werkzeug.utils import secure_filename

# # from models import  Domain,Task




def Domain_reveal(model):
    container = []
    for i in model.query.all() :
        container.append((i.title, i.title))

    return container

def DomainQuery():
    return Domain.query

class  RegistrationForm(FlaskForm):

    username =  StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email =  StringField('Email', validators=[DataRequired(),Email()])
    password1  =PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('confirm password', validators=[DataRequired(),EqualTo('password1')]) 
    submit = SubmitField('Sign Up') 


    def validate_username(self,username):
        
        user =  User.query.filter_by(username=username.data).first() 

        if user:
            raise ValidationError("Username taken, choose another one")
    
    def validate_email(self, email):
        user =  User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError("email already exists")


   

class  LoginForm (FlaskForm):

   
    email =  StringField('Email', validators=[DataRequired(),Email()])
    # username= StringField('Username', validators=[DataRequired()])
    password  =PasswordField('Password', validators=[DataRequired()])
    remember =  BooleanField('Remember me')
    submit = SubmitField('Login')

class TaskProcessorForm(FlaskForm):
    
   
    Ms_name =  StringField(u'Task Name', validators=[DataRequired()])
    NameSpace =  StringField(u'Namespace', )
    purpose =  StringField(u'Purpose', widget=TextArea(),validators=[DataRequired()])
    domain = SelectField(u'Domain Name', choices=Domain_reveal(Domain))
    desired_output =  SelectField(u'Desired Output', choices=[('pipeline','pipeline'),('Data','Data'),('Image','Image'),('Text','Text') ,('5','Any type')], validators=[DataRequired()])
    fileInput =  FileField(u'Input file ', validators=[FileAllowed(['csv','xlsx'])])
    efileInput =  FileField(u'Extra input file ', validators=[FileAllowed(['csv','xlsx'])])
    # gpu = BooleanField()
    submit =  SubmitField('Process Task')



    
     
class DomainForm(FlaskForm):

    title = StringField('Domain Name', validators=[DataRequired()])
    description= StringField("Description", validators=[DataRequired()])
    # created_by =  StringField('Domain Author', validators=[DataRequired()],default=current_user.username if current_user else 'Anonymous')
    submit  = SubmitField("Add Domain")



class ServiceRegistrationForm(FlaskForm):
    Namespace = StringField('NameSpace', render_kw={'placeholder':'the service namespace e.g http://someservicves.ln.uk '})
    Ms_name =  StringField('MicroService Name', render_kw={'placeholder': 'the service name '  })
    Description =  StringField('Description')
    Ms_type =  StringField('Microservice Type', render_kw={'placeholder':'[data loading, data clearning, data trasnfer, data scaling, ... machine learning model,  visulaisation]'})
    Dependencies =  StringField('Dependencies', render_kw={'placeholder':'libaries needed  e.g [sklearn.... pandas.... numpy] seperate with a comma "," '})
    Framework =  StringField('Framework', render_kw={'placeholder':'programming framework needed, seperate with a comma " , "'})
    GPU =  SelectField(u'Turns on the Usage of GPU or not', choices=[(1,'True'),(0,'False')])
    Pipeline =  StringField(u'Pipeline', render_kw={'placeholder':'the microservices composition process of this service. IF = 0, then this is atom service'})
    Model_format  =StringField(u'Model Format', render_kw={'placeholder':'the model save formation e.g. h5 that can be invoked'})
    ServiceCategory =  StringField(u"Service Category", render_kw={'placeholder':"[linearRegression, ... logitstic regression, ... CNN]" }, default="AI category")
    Invoke_uri =  StringField('Invoke Uri', render_kw={'placeholder':'http://someservicves.ln.uk'})
    Input_sp =  SelectField('Input_sp', choices=[('1','Data'),('2','Image'),('3','Text'), ('4','Other type'),('5','Any type')], default=1)

    Output_sp =   SelectField(u'Output_sp', choices=[('1','Data'),('2','Image'),('3','Text'), ('4','Other type'),('5','Any type')],default=4)
    Contributor =  StringField(u"Contributor" ,render_kw={'placeholder':  "organisation or individual or groups who developed this model"})
    License =  StringField("License", render_kw={'placeholder':'License if Available'})
    
    submit =  SubmitField('REGISTER SERVICE')



def upload(name):
    file = request.files['file']

    filename = secure_filename(file.filename)
    new_filename = f'{filename.split(".")[0]}_{str(datetime.now())}.csv'
    save_location = os.path.join('storage/files', new_filename)
    file.save(save_location)



    return 