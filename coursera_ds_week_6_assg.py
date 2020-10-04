10.2 Write a program to read through the mbox-short.txt and figure out the 
distribution by hour of the day for each of the messages. You can pull the hour 
out from the 'From ' line by finding the time and then splitting the string a
second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts,
sorted by hour as shown below.
#%%
fhand=open("mbox-short.txt")
dic={}
list=[]
for line in fhand:
    if line.startswith('From '):
        #print(line)
        word=line.split()
        #print(word)
        #print(len(word))
        word[5]=word[5].split(":")
        list.append(word[5])
#print(list)
for i,j,k in list:
    dic[i]=dic.get(i,0)+1
#print(dic)
for k,v in sorted(dic.items()):
    print(k,v)