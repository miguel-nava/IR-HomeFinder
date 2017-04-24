from bottle import route, run, template
from datafetch import createURL

@route('/hello/<name>')
def index(name):
	return template('<b>Hello {{name}}</b>!', name=name)

@route('/')
def mainPage():
	return template('<b>You are connected to the server {{name}}</b>', name = 'Muhammad');

@route('/string')
def requestString():
	print('request for strig')
	return "You have requested the string"

@route('/request/<city>/<zip>/<bed>/<bath>')
def getHouse(city, zipC, bed, bath):
	return createURL(city,bed,bath,zipC)
	#return template('You are requesting a house in {{city}}, {{zip}}. With {{bed}} bedrooms and {{bath}} baths.', city = city, zip = zipC, bed = bed, bath = bath)

run(host='localhost', port=80)
