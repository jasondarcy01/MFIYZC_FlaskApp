from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from models import User
from utils import get_neighbors, zipcodes

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mfiyzc.db'
db = SQLAlchemy(app)


#link functions to url
@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
      v = int(request.form['number'])
      values = get_neighbors(v, zipcodes)
      print(values)
      results=User.query.filter(User.zipcode.in_(values)).all()
      print(results)
      return render_template('welcome.html', string='Make Friends by Zipcode', value=v, values=values)
    return render_template('index.html', string='Make Friends by Zipcode')

@app.route("/create_profile")
def welcome():
    return render_template("create_profile.html")


if __name__ == "__main__":
     app.run(debug = True)




