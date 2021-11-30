import urllib.request
import json

from test import ip
url = 'http://ip-api.com/json/'
response = urllib.request.urlopen(url + ip)
data = response.read()
rkt = json.loads(data)
print ("")
print (data)
print ("")
print ('Done')
print ("")