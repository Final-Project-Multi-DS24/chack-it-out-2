from ast import Pass
from flask_wtf import FlaskForm # subject, content 속성을 포함함
from wtforms import StringField, TextAreaField, PasswordField, DateField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Regexp, ValidationError

from models.User import User
# DataRequired : 필드값을 검증할 때 사용하는 도구

class LoginForm(FlaskForm):
    userid = StringField(label="아이디", validators=[DataRequired(), Length(min=3, max=25)])
    password = StringField(label="비밀번호", validators=[DataRequired()])
    #html 관련 / 책 104페이지 참고
    
class RegisterForm(FlaskForm):
    username = StringField('이름', validators=[DataRequired(), Length(min=3, max=25)])
    userid = StringField('아이디', validators=[DataRequired()])
    
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('이미 사용 중인 아이디입니다. 다른 아이디를 입력해주세요.')
        
    password1 = PasswordField('비밀번호', validators=[DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호 확인', validators=[DataRequired()])
    phonenumber = StringField('전화번호',validators=[Regexp(r'^\d{3}-\d{3,4}-\d{4}$', message='올바른 전화번호 형식이 아닙니다.')])
    userbirth = DateField('생년월일', format='%Y-%m-%d')
    
    interst = [('cat', '고양이'), ('dog', '개'), ('hamster', '햄스터')]
    selection = SelectMultipleField('관심 키워드를 선택하세요', choices=interst, validators=[DataRequired('하나 이상 선택해주세요.')], option_widget=None) #option_widget=None은 choices의 메뉴 항목을 라디오 버튼 대신 체크박스를 만들도록 설정합니다
    
    # submit = SubmitField('제출')
    