from flask import Blueprint, make_response, jsonify, render_template, redirect, request, url_for, flash, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from models.User import User # 조회할 유저목록
from models.UserInterest import Selection
from forms.registerform import RegisterForm, LoginForm

db = SQLAlchemy()

auth = Blueprint("auth",__name__, url_prefix="/auth")


# api = Api(register)


@auth.route("/register/", methods=['GET','POST']) # 템플릿의 method값과 일치
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit(): #폼데이터의 정합성을 점검: 
        # username = request.form['userid'] #form의 name 속성이 userid 
        # password = request.form['password']
        user = User.query.filter_by(username = form.username.data).first()
        if user is not None:
            return flash("이미 존재하는 사용자입니다")
        else:
            new_user = User(username=form.username.data,
                            userid=form.userid.data, 
                            password=generate_password_hash(form.password1.data),
                            phonenumber=form.phonenumber.data, 
                            userbirth=form.userbirth.data)
            db.session.add(new_user)
            
            for selection in form.selection.data:
                selection = Selection(user = user, interest = interest)
                db.session.add(selection)
            
            db.session.commit()
            return redirect(url_for('login.html'))
    return render_template('register.html', form = form) #get방식으로 요청되었을 떄
    
@auth.route("/login/", methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.fillter_by(userid = form.userid.data).first()
        if not user:
            error = "아이디가 존재하지 않습니다."
        elif not check_password_hash(user.password, form.password.data):
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            session.clear()
            session['user_pk'] = user.userpk
            return redirect(url_for('main.index'))
        flash(error)
    return render_template('login.html', form=form)

@auth.before_app_request # 모든 라우터보다 먼저 실행됨
# g는 플라스크가 제공하는 컨텍스트 변수
def load_logged_in_user():
    userpk = session.get('user_pk')
    if userpk is None:
        g.user = None
    else:
        g.user = User.query.get(userpk)
        
@auth.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('main.index'))