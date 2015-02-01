from thing import db

class User(db.Model):

  __tablename__ = "users"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  zipcode = db.Column(db.Integer, nullable=False)
  inter1 = db.Column(db.String, nullable=False)
  inter2 = db.Column(db.String, nullable=False)
  inter3 = db.Column(db.String, nullable=False)

  def __init__(self, name, zipcode, inter1, inter2, inter3):
    self.name = name
    self.zipcode = zipcode
    self.inter1 = inter1
    self.inter2 = inter2
    self.inter3 = inter3

  def __repr__(self):
    return '<{},{},{},{},{}'.format(self.name, self.zipcode, self.inter1, self.inter2, self.inter3)