s1=input('inserire stringa1: ')
s2=input('inserire stringa2: ')
contatore=0
somma=' '
for i in range(0,len(s1)):
    for j in range(i+1, len(s1)+1):
        s= s1[i:j]
        if s in s2:
            l=j-i
            if l>=contatore:
                contatore=l
                somma=s
        else:
            break
print(somma)
            
