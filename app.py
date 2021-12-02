from flask import Flask,render_template,request
from flask_wtf import FlaskForm  
from wtforms import StringField,SubmitField

app=Flask(__name__)
app.config['SECRET_KEY']='private_key'

#create form class
class NameForm(FlaskForm):
    name=StringField('UserName')
    submit=SubmitField('Submit')

#Create name page
@app.route('/name',methods=['GET','POST'])
def name():
    form=NameForm()
    #validate
    if request.method=='POST':
        name=form.name.data
        form.name.data=''
        if form.validate()==False:

            return render_template('hello.html',form=form,name=name)
        else:
            return render_template('user.html',name=name)
    return render_template('hello.html',form=form)




if __name__=='__main__':
    app.run(port=1234,debug=True)