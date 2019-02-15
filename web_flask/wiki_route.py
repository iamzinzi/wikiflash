"""
starts a Flash web app
"""
from flask import flask, render_template, request
app = Flask(__name__)
from get_path import get_path
app.url_map.strict_slashes = False


@app.route('/web_flask/s_word/<s_word>/e_word/<e_word>', methods=["GET"])
def result(state_id):
    """return the function"""
    result = request.form
    lis = get_path(s_word, e_word)
    return render_template('index.html', lis)


if __name__ == '__main__':
    app.run(host="35.235.70.198", port=5000)
