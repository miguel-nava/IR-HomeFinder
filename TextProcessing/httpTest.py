from urllib2 import *
import fileinput

mainPage = "http://34.208.154.237/"

var = "request/houston/77099/2/1"
result = urlopen(mainPage + var)
print result.read()

# for line in fileinput.input():
	# result = urlopen(mainPage)
	# print(result.read());
