from flask_sqlalchemy import SQLAlchemy

from web.Book.models.UserInterest import UserInterest

db = SQLAlchemy()

# 로그인시 필요한 유저정보를 조회
# 회원가입시 필요한 유저정보 등록

# userpk, userid, passwd, birth, preference, email??

class User(db.Model):
    """_summary_

    Args:
        db (_type_): _description_
    """
    __tablename__ : "user"
    
    userpk = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10),unique=True, nullable=False)
    userid = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    phonenumber = db.Column(db.String(20))
    userbirth = db.Column(db.DateTime)
    userinterest = db.relationship('Selection',backref = 'user')
    

    # def __init__(self, userid, password):
    #     self.userid = userid
    #     self.password = password
        
        
