from flask import Flask, request, make_response, session, render_template, abort, url_for
from flask.json import jsonify, loads
from sys import getsizeof
import pandas as pd


app = Flask(__name__)
app.secret_key = b'_5#H2G"F4Q8z\n\xec]/'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['csv_file']

        if (file.content_type == 'text/csv') and (getsizeof(file) < 32000000):
            json_file = pd.read_csv(file).to_json()
            return loads(json_file)
        else:
            return abort(400)

    elif request.method == 'GET':
        return render_template('index.html')

    else:
        return abort(400) 

if __name__ == "__main__":
    app.run(threaded=True, port=5000)
