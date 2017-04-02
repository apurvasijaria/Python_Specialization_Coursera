import urllib2

request = urllib2.Request('http://data.pr4e.org/intro-short.txt')
request.add_header('User-Agent', 'some fake agent string')
request.add_header('Referer', 'fake referrer')
response = urllib2.urlopen(request)
# check content type:
print 'Contecnt-Type',response.info().getheader('Content-Type')
print 'Contecnt-Length',response.info().getheader('Content-Length')
print 'Last-Modified',response.info().getheader('Last-Modified')
print 'ETag',response.info().getheader('ETag')