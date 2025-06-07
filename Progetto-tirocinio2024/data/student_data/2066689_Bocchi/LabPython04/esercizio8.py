s= input('stringa: ')
x= 1
y= 0

while y != x:
    x= s[-1]
    s2=s
    s= input('stringa: ')
    y= s[0]
    
print(s2, s)
