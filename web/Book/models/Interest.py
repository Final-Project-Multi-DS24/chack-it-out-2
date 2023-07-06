from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Interest(db.Model):
    ''' interest table
    - interest_id : 선호 키워드 id
    - interest_name : 선호 키워드 이름
    '''

    __tablename__ = "interest"

    interest_id = db.Column(db.Integer, nullable=False,
                         autoincrement=True, primary_key=True)
    interest_name = db.Column(db.String(255))

    def __repr__(self):
        return f"[Interest] ({self.interest_id}, {self.interest_name})"