import urllib
import beautifulsoup

url = raw_input('Enter - ')
if len(url)<1:url='http://python-data.dr-chuck.net/known_by_Fikret.html'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print tag.get('href', None)