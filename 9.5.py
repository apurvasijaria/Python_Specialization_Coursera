#9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
#fter the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
fname = raw_input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
handle = open(fname)
text = handle.read()
words = list()

for line in handle:
    if not line.startswith("From ") : continue
    line = line.split()
    words.append(line[1])

counts = dict()

for word in words:
    counts[word]=counts.get(word,0)+1


maxvalue = None
maxkey = None

for key,value in counts.items() :
  if value > maxvalue:
    print value
    maxvalue = value
    maxkey = key


print maxkey, maxvalue