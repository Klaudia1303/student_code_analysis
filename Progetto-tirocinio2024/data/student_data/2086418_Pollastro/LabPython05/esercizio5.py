s=str(input('inserire stringa: '))
n=int(input('inserire intero positivo: '))
for i in range(len(s)):
    if int(i+n)< int(len(s)) and s[i]==s[int(i+n)]:
        print('True')
    if int(i+n)> int(len(s)):
        print('False')

    
