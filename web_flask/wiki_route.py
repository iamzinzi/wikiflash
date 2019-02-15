"""
starts a Flash web app
"""
from flask import flask, render_template, jsonify
app = Flask(__name__)
import function
app.url_map.strict_slashes = False



@app.errorhandler(404)
def not_found(error):
    """Gives error message when any invalid
    url are requested
    """
    return jsonify({"error": "Not found"}), 404


@app_views.route('/s_word/<s_word>/e_word/<e_word>', methods=["GET"])
def return_cities(state_id):
    """return the function"""
    dic = {"s_word": sword, "e_word": e_word}
    lis = function(dic)
    if lis is None:
        abort(404)
    else:
        return render_template('index.html', lis)


if __name__ == '__main__':
    app.run(host="35.235.70.198", port=4000)
