from datetime import datetime
from bson.json_util import dumps
from flask import Flask, render_template, request, redirect, url_for,session,flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_socketio import SocketIO, join_room, leave_room
from pymongo.errors import DuplicateKeyError
from functools import wraps
import time

import pandas as pd
import os
from csv import writer
import random

from db import get_user, save_user, save_room, add_room_members, get_rooms_for_user, get_room, is_room_member, \
    get_room_members, is_room_admin, update_room, remove_room_members, save_message, get_messages

app = Flask(__name__)
app.secret_key = "sfdjkafnk"
socketio = SocketIO(app)
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

#Questions
data=pd.read_csv('bm.csv')
records=data.to_records(index=False)
result = list(records)
q1=random.choice(result)
q2=random.choice(result)
coding=pd.read_csv('coding.csv')
coding_records=coding.to_records(index=False)
code_result = list(coding_records)
q3=random.choice(code_result)
q4=random.choice(code_result)
current=pd.read_csv('ca.csv')
current_records=current.to_records(index=False)
current_result = list(current_records)
q5=random.choice(current_result)
q6=random.choice(current_result)
verbel=pd.read_csv('verbel.csv')
verbel_records=verbel.to_records(index=False)
verbel_result = list(verbel_records)
q7=random.choice(verbel_result)
q8=random.choice(verbel_result)

# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap

#Homepage
@app.route('/')
def home():
    return render_template('index.html')

#Projects page
@app.route('/projects')
def projects():
    return render_template('projects.html')

#add student representative
@app.route('/addstudent',methods=['GET', 'POST'])
@login_required
def add_student():
    if request.method == 'POST':
        image = request.files['img']
        name = request.form.get('name')
        year = request.form.get('year')
        branch =  request.form.get('branch')
        phno= request.form.get('phno')
        email= request.form.get('email')
        filename = name + ".jpg"
        newfilename = os.path.join('static/images/student', filename)
        image.save(newfilename)
        
        added_name=current_user.username
        # points = str(name,year,branch,phno,email)
        with open('stu_co.csv','r+') as f:
            myDataList=f.readlines()
            nameList=[]
            for line in myDataList:
                entry = line.split(',') 
                nameList.append('added') 
            
            if name not in nameList:
                now =datetime.now()
                dtString=now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dtString},{year},{branch},{phno},{email},{added_name}')
            
        
        return "added successfully"
        
    return render_template('addstudent.html')

#Team Rankking
@app.route('/team_rank')
def team_rank():
    return render_template('team_rank.html')

#add student representative
@app.route('/addteacher',methods=['GET', 'POST'])
@login_required
def add_teacher():
    if request.method == 'POST':
        image = request.files['img']
        name = request.form.get('name')
        branch =  request.form.get('branch')
        phno= request.form.get('phno')
        email= request.form.get('email')
        filename = name + ".jpg"
        newfilename = os.path.join('static/images/teacher', filename)
        image.save(newfilename)
        
        added_name=current_user.username
        # points = str(name,year,branch,phno,email)
        with open('tea_co.csv','r+') as f:
            myDataList=f.readlines()
            nameList=[]
            for line in myDataList:
                entry = line.split(',') 
                nameList.append('added') 
            
            if name not in nameList:
                now =datetime.now()
                dtString=now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dtString},{branch},{phno},{email},{added_name}')
            
        
        return "added successfully"
        
    return render_template('addteacher.html')    

#Registration page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    message = ''
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        usn = request.form.get('usn')
        name = request.form.get('name')
        branch = request.form.get('branch')
        try:
            save_user(username, email, password,usn,name,branch)
            return redirect(url_for('login'))
        except DuplicateKeyError:
            message = "User already exists!"
    return render_template('registration.html', message=message)

#Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    message = ''
    if request.method == 'POST':
        username = request.form.get('username')
        password_input = request.form.get('password')
        user = get_user(username)

        if user and user.check_password(password_input):
            login_user(user)
            return redirect(url_for('home'))
        else:
            message = 'Failed to login!'
    return render_template('login1.html', message=message)

#Test
@app.route('/test')
@login_required
def test():
    return render_template('quiz.html',q1=q1,q2=q2,q3=q3,q4=q4,q5=q5,q6=q6,q7=q7,q8=q8,q9=q4,q10=q4)

#TEAM
@app.route('/team')
def team():
    return render_template('team.html')

#Result
@app.route('/marks')
@login_required
def marks():
    score=pd.read_csv('answer.csv')
    score1=score.to_records(index=False)
    result = list(score1)
    # lists1 = list.sort_values("marks", ascending=True)
    return render_template('result.html',results=result)


#Fetch Teacher Coordinators
@app.route('/fetch_teacher')
@login_required
def teacher():
    score=pd.read_csv('tea_co.csv')
    score1=score.to_records(index=False)
    result = list(score1)
    # lists1 = list.sort_values("marks", ascending=True)
    return render_template('teacher_team.html',results=result)

#Fetch Teacher Coordinators
@app.route('/fetch_student')
@login_required
def student():
    score=pd.read_csv('stu_co.csv')
    score1=score.to_records(index=False)
    result = list(score1)
    # lists1 = list.sort_values("marks", ascending=True)
    return render_template('student_team.html',results=result)



#Score of the test
@app.route('/answer',methods=['GET','POST'])
@login_required
def answer():
    if request.method == "POST":
        qes1=request.form.get('q1')
        qes2=request.form.get('q2')
        qes3=request.form.get('q3')
        qes4=request.form.get('q4')
        qes5=request.form.get('q5')
        qes6=request.form.get('q6')
        qes7=request.form.get('q7')
        qes8=request.form.get('q8')
        qes9=request.form.get('q9')
        qes10=request.form.get('q10')
        points=0
        if (q1[6]==qes1):
            points=points+10
        if (q2[6]==qes2):
            points=points+10
        if (q3[6]==qes3):
            points=points+10
        if (q4[6]==qes4):
            points=points+10
        if (q5[6]==qes5):
            points=points+10
        if (q6[6]==qes6):
            points=points+10
        if (q7[6]==qes7):
            points=points+10
        if (q8[6]==qes8):
            points=points+10
        if (q1[6]==qes1):
            points=points+10
        if (q1[6]==qes1):
            points=points+10
        
        name=current_user.username
        points = str(points)
        with open('answer.csv','r+') as f:
            myDataList=f.readlines()
            nameList=[]
            for line in myDataList:
                entry = line.split(',') 
                nameList.append('added') 
            
            if name not in nameList:
                now =datetime.now()
                dtString=now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dtString},{points}')
            
        
        return redirect('/score')
    return "Not working yet"

#thank you for the submittion
@app.route('/score')
@login_required
def score():
    return render_template('score.html')

#Logout
@app.route("/logout/")
@login_required
def logout():
    logout_user()
    session.clear()
    flash("Successfully Logged out!!!")
    return redirect(url_for('home'))

@login_manager.user_loader
def load_user(username):
    return get_user(username)


if __name__=="__main__":
    app.run(debug=True)
