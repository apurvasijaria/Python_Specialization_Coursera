import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address=raw_input('Enter Location:')
    if len(address)<1:break

    url=serviceurl+urllib.urlencode({'sensor':'false','address':address})
    print 'Retreiving',url
    uh=urllib.urlopen(url)
    data=uh.read()
    print 'Retreiving',len(data),'charaters'

    try: js=json.loads(str(data))
    except: js=None
    input=js['results']
    print input[0]['place_id']


