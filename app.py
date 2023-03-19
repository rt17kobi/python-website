from flask import Flask, render_template

# declaring the variable app which can inherit the Flask properties.
app = Flask(__name__)


# @-> decorators
@app.route("/")
def hi():
  return render_template('home.html')


# to run the app on local host
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
