

import urllib
from BeautifulSoup import *

url = raw_input('Enter : ')
html=urllin.urlopen(url).read()
sum=0
count=0
soup=BeautifulSoup(html)


tags=soup('span')
for tag in tags:
    count=count+1
    sum=sum+tag.content[0]

print count
print sum

