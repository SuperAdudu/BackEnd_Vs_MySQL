from source import db

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    link = db.Column(db.String(250), nullable=False)