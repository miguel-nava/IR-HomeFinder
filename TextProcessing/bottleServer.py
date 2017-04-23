from bottle import route, run, template

@route('/hello/<name>')
def index(name):
	return template('<b>Hello {{name}}</b>!', name=name)

@route('/')
def mainPage():
	return template('<b>You are connected to the server {{name}}</b>', name = 'Muhammad');

run(host='localhost', port=65530)