s=input('inserire stringa: ')
n=1

while s.find('c')<0 or s.find('a')<0:
    s=input('inserire stringa: ')
    n+=1
print(n)
