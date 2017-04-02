import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter URL ')
if len(url) < 1 : url='http://python-data.dr-chuck.net/comments_42.xml'


uh = urllib.urlopen(url)
data = uh.read()
stuff=ET.fromstring(data)


sum=0
counts = stuff.findall('.//comment')
for values in counts:
    b= int(values.find('count').text)
    sum=sum+b
print sum

