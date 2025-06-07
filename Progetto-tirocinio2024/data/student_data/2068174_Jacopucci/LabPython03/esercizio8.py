str1=input('inserire una stringa palindroma: ')
c=len(str1)
c1=str(c)
str2=str1[::]
n=0
while (n==1):
    if (str1==str2):
        print ('la stringa è palindroma ed è lunga '+c1)
        n+=1
    else:
        str1=input('stringa non palindroma, inserire una stringa palindroma: ')
        
