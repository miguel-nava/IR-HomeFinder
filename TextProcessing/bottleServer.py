from bottle import route, run, template
from datafetch import createURL

@route('/')
def mainPage():
	return template('You have connected to the server')

@route('/request/<city>/<zipC>/<bed>/<bath>')
def getHouses(city, zipC, bed, bath):
	return createURL(city,bed,bath,zipC)


run(host='localhost', port=8080)
