s1=input("inserisci stringa: ")
s2=input("Inserisci stringa: ")

for i in range(1,len(s1)):
    if s2.find(s1[i])==s2.find(s1[i-1]):
        print(s2[s2.find(s1[i])])
    
    
    
