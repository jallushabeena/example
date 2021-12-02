from flask import Flask,render_template,request
from flask_wtf import FlaskForm  
from wtforms import StringField,SubmitField

app=Flask(__name__)
app.config['SECRET_KEY']='66f90831bf9d57902846ad4bb94dbd51ec4e0235b3a6205c538e273ed79e31ee38b1a885ea8225819775a068ca761eaec89e7f99a93503e4c28fe9df'

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