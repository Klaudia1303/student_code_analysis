s1=input("stringa a: ")
s2=input("stringa b: ")
lun=0
ris=""
for i in range(len(s1)):
    for n in range(i+1,len(s1)):
        if s2.find(s1[i:n])!=-1 and len(s1[i:n])>lun:
            lun=len(s1[i:n])
            ris=s1[i:n]
        else:
            continue
print(ris)
        
