from bottle import route, run, template
from bottledaemon import daemon_run
from datafetch import createURL

@route('/')
def mainPage():
	return template('You have connected to the server')

@route('/request/<city>/<zipC>/<bed>/<bath>')
def getHouses(city, zipC, bed, bath):
	return createURL(city + ",%20" + "tx",bed,bath,zipC)


daemon_run(host='0.0.0.0', port=80)
# run(host='0.0.0.0', port=80)
