s=input('inserisci una stringa ')
k=1
i=0
while i<(len(s)) and k==1:
    if s.find(s[i])!=s.rfind(s[i]):
        print(True)
        k=2
    i+=1
if k==1:
    print(False)
   
