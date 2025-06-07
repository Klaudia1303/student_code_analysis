s=input("inserire una stringa: ")
n=int(input("inserire un numero intero: "))
i=0
corretto=True
while (i+n)<len(s):
    if s[i]==s[i+n] and corretto:
        print(True)
        corretto=False
    i+=1
if corretto==True:
    print(False)
        
