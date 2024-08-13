from flask import Flask, render_template
import requests

app = Flask(__name__)

all_posts = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391').json()


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/post/<blog_id>')
def blog_post(blog_id):
    return render_template("post.html", post=all_posts[int(blog_id)-1])


if __name__ == "__main__":
    app.run(debug=True)
