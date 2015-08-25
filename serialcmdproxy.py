import urllib
import urllib2
import serial

device_id = '123456'
kill = False

ser = serial.Serial(
    port='/dev/ttyACM0', 
    baudrate=115200,
    timeout=1,    
)

ser.write("hello")      # write a string

while not kill:
	# if not ser.inWaiting():
	line = ser.readline()
	if len(line):
		print line,


ser.close()             # close port


url = "http://localhost:8000/api/device/" +device_id+ "/update"
values = {'name' : 'Michael Foord',
		'location' : 'Northampton',
          'language' : 'Python' }
headers = { 'User-Agent' : user_agent }

data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page