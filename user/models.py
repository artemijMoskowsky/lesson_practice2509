from main.settings import DATABASE

from flask_login import UserMixin

class User(DATABASE.Model, UserMixin):
    
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    
    username = DATABASE.Column(DATABASE.String(80), nullable = False)
    
    password = DATABASE.Column(DATABASE.String(55), nullable = False)
    
    def __repr__(self):
        
        return f"ID - {self.id}, Name - {self.username}"