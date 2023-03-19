from flask import Flask

# declaring the variable app which can inherit the Flask properties.
app = Flask(__name__)


# @-> decorators
@app.route("/")
def hi():
  return "Hi Rohan Tiwari"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
