from urllib.request import urlopen
import fileinput

mainPage = "http://localhost:65530/"

for line in fileinput.input():
	words = line.split(' ')
	result = urlopen(mainPage+line)
	print(result.read());
