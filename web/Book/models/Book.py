from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    """_summary_

    Args:
        db (_type_): _description_
    """
    
    __tablename__ : "book"
    
    book_isbn = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    book_title = db.Column(db.Integer, nullable=False)
    book_author = db.Column(db.Integer, nullable=False)
    book_publisher = db.Column(db.String(255), nullable=False)
    book_contents = db.Column(db.Text())
    book_date = db.Column(db.DateTime)
    book_cover = db.Column(db.Text())
    book_description = db.Column(db.Text())

    #해당 클래스에 대해 string 값으로 대표되는 값을 표현
    def __repr__(self):
        return f"[Book] ({self.book_isbn}, {self.book_title}, {self.book_author}, {self.book_publisher}, {self.book_date}, {self.book_cover})"

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}

    # def as_simple_dict(self, idx):
    #     rank = {"rank": idx}
    #     return dict({x.name: getattr(self, x.name) for x in self.__table__.columns if x.name not in ['book_contents', 'book_description', 'book_date']}, **rank)
