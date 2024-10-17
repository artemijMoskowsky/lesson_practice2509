from main.settings import DATABASE

class Trip(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    title = DATABASE.Column(DATABASE.String(40))
    date = DATABASE.Column(DATABASE.String(40))
    country = DATABASE.Column(DATABASE.String(40))
    price = DATABASE.Column(DATABASE.String(40))
    description = DATABASE.Column(DATABASE.Text)

    def __repr__(self):
        return f"id = {self.id}, title = {self.title}, date = {self.date}, country = {self.country}"