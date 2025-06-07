s=input('inserire una stringa:')
n=0
while s.find('a')==-1 or s.find('c')==-1:
    s=input('inserire una stringa:')
    n+=1
print(n+1)
