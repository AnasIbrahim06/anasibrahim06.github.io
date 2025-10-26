<<<<<<< HEAD
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

if __name__ == "__main__":
=======
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

if __name__ == "__main__":
>>>>>>> 9d79de27db77a1c472c4358bdfb2b37ace8509d7
    app.run(debug=True)