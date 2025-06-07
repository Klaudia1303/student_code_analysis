s1=s2=s3=s4='a'
i=1
while len(s3)+len(s2)!=len(s1):
    s1= input ('Inserisci una stringa :')
    if i == 1 :
        s2 = s1
    elif i == 2:
        s3=s2
        s2=s1
    elif i ==3 :
        s4=s1
    elif i >3:
        s3=s2
        s2=s4
        s4=s1
    i=i+1
print (s3,s2,s1)
