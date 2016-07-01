import urllib2
import time
import json

#request = urllib2.Request('http://localhost:8080/measurement/loss/set/1/2')
#response = urllib2.urlopen(request)
for i in range(50):
    #request = urllib2.Request('http://localhost:8080/measurement//set/1/2')
    #response = urllib2.urlopen(request)
    #result = response.read()
    #encodedjson = json.dumps(result)
    html = urllib2.urlopen('http://localhost:8080/measurement/delay/1/2')
    hjson = json.loads(html.read())
    print hjson['delay_result']
    time.sleep(1)