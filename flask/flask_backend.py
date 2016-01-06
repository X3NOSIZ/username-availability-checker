from flask import Flask, request, render_template
from jinja2 import Template
import requests
from flask.ext.cors import CORS, cross_origin

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
cors = CORS(app) #, resources={r"/api/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def my_form():
    return render_template("myform.html")

@app.route('/', methods=['POST'])
@cross_origin(origin='*')
def my_form_post():
	username = request.form['text']
	return render_template('world.html', username = username)

if __name__ == "__main__":
	app.run(debug=True, port=8080)
	logging.getLogger('flask_cors').level = logging.DEBUG