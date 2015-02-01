from app import db
from models import User

#create the db and tables
db.create_all()

#insert
db.session.add(User("Jane Parker", 11104, "ice skating", "dancing", "reading"))
db.session.add(User("Bob Smith", 11104, "boxing", "cars", "beers"))


# commit the changes
db.session.commit()