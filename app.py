from flask import Flask, render_template, request
app = Flask(__name__)



@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
      v = int(request.form['number'])
      return render_template('welcome.html', string='Make Friends by Zipcode', value=v)
    return render_template('index.html', string='Make Friends by Zipcode')

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

if __name__ == "__main__":
     app.run(debug = True)



# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World!"

# if __name__ == "__main__":
#     app.run(debug = True)