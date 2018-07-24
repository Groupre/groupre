import groupre
from datetime import datetime
from flask import Flask, render_template,make_response,request, url_for, flash, redirect
# from flask_sqlalchemy import SQLAlchemy
from flaskForm import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# db = SQLAlchemy(app)



# def transform(student, chair):
#     # merged = student.merge(chair)
#     ARGS = ['-c',chair, '-s',student, '-o', output.csv]
#     groupre.main(ARGS)
    
#     return output.csv

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/room_builder")
def about():
    return render_template("room_builder.html")

@app.route("/demo")
def demo():
    return render_template("builderDemo.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/transform" , methods = ["POST"])
def transform_view():
    student_file = request.files['student_file']
    chair_file = request.files['chair_file']
    if not student_file:
        return "no student csv files"
    elif not chair_file:
        return "no chair csv files"
    
    # student_file_contents = student_file.stream.read().decode("utf-8")
    # chair_file_contents = chair_file.stream.read().decode("utf-8")
    ARGS = ['-c','chair_file', '-s','student_file', '-o', "output"]
    groupre.main(ARGS)
    print('This works')
    # result = transform(student_file_contents,chair_file_contents)
    response = make_response(output)
    response.headers["Content-Disposition"] = "attachment; filename=result.csv" 
    return response

if __name__ == '__main__':
    app.run(debug=True)
