import re

hand=open('mbox-short.txt')
for line in hand:
    line=line.strip()
    if re.search('From:',line):
        print line