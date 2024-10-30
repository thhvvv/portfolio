from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Farmer(db.Model):
    __tablename__ = 'farmers'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    profile_pic = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<Farmer {self.username}>'

