s=input('inserire una stringa ')
n=int(input('inserire un intero positivo '))
i=0
a=True
while(i+n)<len(s):
    if s[i]==s[i+n] and a:
        print(True)
        a=False
    i+=1
if a==True:
    print(False)
