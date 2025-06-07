s1=input("Inserisci una stringa : ")
s2=input("Inserisci una stringa : ")
s3=""
for i in range(len(s1)):
    if(s2.find(s1[i])==-1):
        s3+=s1[i]
print(s3)