from flask import Flask, render_template
import requests

app = Flask(__name__)

data = requests.get(url='https://api.npoint.io/145c3b8db6eb519f1031').json()


@app.route('/')
def home():
    return render_template("index.html", posts=data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:_id>")
def post(_id):
    return render_template("post.html", post=data[_id-1])


if __name__ == "__main__":
    app.run()
