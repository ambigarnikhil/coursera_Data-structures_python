Open the file romeo.txt and read it line by line. For each line, split the line
into a list of words using the split() method. The program should build a list
of words. For each word on each line check to see if the word is already in
the list and if not append it to the list. When the program completes, sort
and print the resulting words in alphabetical order.
 #%%
fname=input("Enter the file name :")
fhand=open(fname ,"r")
a=[]
for i in fhand:
    i=i.strip()
    j=i.split()
    for j in i:
        if j not in a:
            a.append(j)
print(a.sort())
#%%
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    line = line.split()
    for i in line: # observe indentation here
        if i not in lst:
            lst.append(i)
            
lst.sort() # observe indentation here.  this is where i made mistakes..
print(lst)
