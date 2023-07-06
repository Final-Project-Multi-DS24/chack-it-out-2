from ast import Pass
from flask_wtf import FlaskForm # subject, content 속성을 포함함
from wtforms import StringField, TextAreaField, PasswordField
# from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email
# DataRequired : 필드값을 검증할 때 사용하는 도구

# class LoginForm(FlaskForm):
#     id = StringField(label="userid", validators=[DataRequired()])
#     passwd = StringField(label="password", validators=[DataRequired()])
    #html 관련 / 책 104페이지 참고
    
class UserRegisterForm(FalskForm):
    username = StringField('이름', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호 확인', validators=[DataRequired()])
    