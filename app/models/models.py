
from .. import db


# Create a User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    # def __repr__(self):
    #     return f"User('{self.name}', '{self.email}')"
    def to_dict(self):
        return {
            # "id": self.id,
            "name": self.name,
            "email": self.email
            # "username": self.username
        }