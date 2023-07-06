from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Selection(db.Model):
    ''' user_genre table
    - user_interest_id : pk
    - user_id : user id
    - interest_id : interest id
    '''

    __tablename__ = "user_select_interest"

    user_ineterest_id = db.Column(db.Integer, nullable=False,
                              autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.userpk'),nullable=False)
    interest = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"[UserInterest] ({self.user_ineterest_id}, {self.user_id}, {self.interest})"