9.4 Write a program to read through the mbox-short.txt and figure out who has
sent the greatest number of mail messages. The program looks for 'From ' lines
and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address 
to a count of the number of times they appear in the file. After the dictionary 
is produced, the program reads through the dictionary using a maximum loop to
find the most prolific committer.
#%%
fhand=open("mbox-short.txt")
dic={}
list=[]
for line in fhand:
    if line.startswith('From:'):
        word=line.split()
        #print(word)
        #print(len(word))
        list.append(word[1])
#print(list)
for i in list:
    dic[i]=dic.get(i,0)+1
print(dic)

bigcount = None
bigword = None
for word,count in dic.items(): 
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print (bigword,bigcount)