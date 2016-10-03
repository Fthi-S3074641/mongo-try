from flask import Flask
from flask.ext.pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'flmdb'
app.config['MONGO_URI'] = 'mongodb://addmin:addmin@ds013414.mlab.com:13414/flmdb'

mongo = PyMongo(app)

@app.route('/add')
def add():
	user = mongo.db.users
	user.insert({'name' : 'fitu', 'language' : 'python'})
	user.insert({'name' : 'matu', 'language' : 'c'})
	user.insert({'name' : 'katu', 'language' : 'java'})
	user.insert({'name' : 'situ', 'language' : 'c++'})
	user.insert({'name' : 'mitun', 'language' : 'c'})

	return 'added user!'

if __name__ == '__main__':
	app.run(debug=True)