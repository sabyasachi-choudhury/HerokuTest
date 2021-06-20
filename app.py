from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/hello_world')
def hello():
    return 'Hello world'


@app.route('/<url_name>')
def grab_url(url_name):
    return f"Hello {url_name}!"


@app.route('/exp', methods=['POST', 'GET'])
def exp():
    if request.method == 'POST':
        user_name = request.form["name"]
        return redirect(url_for("grab_url", url_name=user_name))
    else:
        return render_template("exp.html")


if __name__ == '__main__':
    app.run()