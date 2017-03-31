def openFile():
    fname = raw_input("Enter file name: ")
    if len(fname) < 1 : fname = "mbox-short.txt"
    try:
        fh = open(fname, 'r')
    except:
        print "Error opening file", fname
        quit()
    return fh

def startsWith():
    sw = raw_input("Enter line prefix to consider: ")
    if len(sw) < 1 : sw = "From"
    return sw

def countTimes(lines,s):
    counts = dict()
    for line in lines:
        if line.startswith(s) and not line.startswith(s+':'):
            line = ((line.rstrip()).lstrip()).split()
        str = line[5]
        hour = str[0:str.find(":"):1]
            counts[hour] = counts.get(hour,0) + 1
    return counts

def sortTimes(d):
    lst = list()
    for key, val in d.items():
        lst.append((key,val))
    lst.sort()
    for val,key in lst:
        print val,key

fh = openFile()
sw = startsWith()
dictionary = countTimes(fh,sw)
t = sortTimes(dictionary)
