from bottle import route, run, template
from datafetch import createURL

@route('/')
def mainPage():
	return template('You have connected to the server')

@route('/request/<city>/<zipC>/<bed>/<bath>')
def getHouses(city, zipC, bed, bath):
	return createURL(city,bed,bath,zipC)

<<<<<<< HEAD
run(host='0.0.0.0', port=80)
=======

run(host='localhost', port=8080)
>>>>>>> 6fac49611c2b7f08f3819d6d9fe7720d9d9fdd65
