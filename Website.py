from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def Contact():

    return render_template("contact.html")


@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/index")
def index():
    return render_template("index.html")

app.run(debug=True)
