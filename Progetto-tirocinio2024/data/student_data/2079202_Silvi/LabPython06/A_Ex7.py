s1=input("inserire prima stringa: ")
s2=input("inserire secondo stringa: ")
cont=0
ris=["",0]
for i in range(0, 1000):
    if s2.find(s1[i]):
        cont+=1
        ris[0]=ris[0]+s1[i]
        for y in range(0, len(s2)-1):
            if s2[s2.find(s1[0])+y]==s1[i+y]:
                cont+=1
                ris[0]=str(ris[0])+s1[i+y]
            else:
                break
    if cont>ris[1]:
        ris[1]=cont
