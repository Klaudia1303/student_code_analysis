s1=input("inserisci stringa:")
i=0
while True:
    s2=input("inserisci stringa:")
    i+=1
    if s1[-1]==s2[0]:
        print(s1,s2)
        break
    else:
        s1=s2
    
