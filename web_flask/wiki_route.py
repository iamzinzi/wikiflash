"""
starts a Flash web app
"""
from flask import Flask, render_template, request
app = Flask(__name__)
from get_path import get_path
app.url_map.strict_slashes = False


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def result():
    """return the function"""
    s_word = request.form['s_word']
    e_word = request.form['e_word']
    lis = get_path(s_word, e_word)
    return render_template('index.html', lis)


if __name__ == '__main__':
    app.run(host="35.235.70.198", port=5000)
