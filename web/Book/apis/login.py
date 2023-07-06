from flask import Blueprint, make_response, jsonify, render_template, redirect, request, url_for
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy

from web.Book.forms.loginform import LoginForm

db = SQLAlchemy()

from models.User import User # 조회할 유저목록

login = Blueprint("login", __name__, url_prefix='/login')
api = Api(login)


@login.route("", methods=['GET','POST']) # 템플릿의 method값과 일치
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit()#폼데이터의 정합성을 점검: 
        username = request.form['userid'] #form의 name 속성이 userid 
        password = request.form['password']
        user = User.query.filter_by(userid=user.userpk).first()
        if user is not None:
            return "이미 존재하는 사용자입니다"
        else:
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            return "가입이 완료되었습니다"
    return render_template('login.html', form = form) #get방식으로 요청되었을 떄
    
@login.route("/logout", methods=['GET'])
def logout():
    session.pop
    return redirect('/') #