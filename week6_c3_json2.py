import urllib
import json

url=raw_input('Enter url:')
sum=0
count=0
print 'Retreiving',url
uh=urllib.urlopen(url)
data=uh.read()
print 'Retreiving',len(data),'charaters'
try:
  js=json.loads(data)
except:
  js=None

input=js['comments']
for var in input:
    b= var['count']
    sum=sum+b
print sum
