from bottle import route, run, template
import datafetch

@route('/hello/<name>')
def index(name):
	return template('<b>Hello {{name}}</b>!', name=name)

@route('/')
def mainPage():
	return template('<b>You are connected to the server {{name}}</b>', name = 'Muhammad');

@route('/string')
def requestString():
	return "You have requested the string"

@route('/request/<city>/<zip>/<bed>/<bath>')
def getHouse(city, zip, bed, bath):
	return template('You are requesting a house in {{city}}, {{zip}}. With {{bed}} bedrooms and {{bath}} baths.', city = city, zip = zip, bed = bed, bath = bath)

run(host='0.0.0.0', port=80)
