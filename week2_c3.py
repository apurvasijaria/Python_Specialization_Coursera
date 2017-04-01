import re

def openfile():
    fname=raw_input('Enter file name:')
    try:
        fh=open(fname)
    except:
        print('Cannot find file')
        quit()
    return fh

def addnumber(lst1):
    sum=0
    for word in lst1:
        number=int(word)
        sum=sum+number
    return sum

def savenumbers(fh):
    lst=list()
    sum1=0
    count=0
    for line in fh:
        line1=line.strip()
        lst=re.findall('[0-9]+',line1)
        if (len(lst)>0):
            add1=addnumber(lst)
        else:
            continue
        sum1=sum1+add1
    return sum1

fh=openfile()
addnum=savenumbers(fh)
print addnum