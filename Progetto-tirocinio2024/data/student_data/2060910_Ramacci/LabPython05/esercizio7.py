s=input("inserire una stringa: ")
corretto=True
for i in range(len(s)):
    if s.count(s[i])>1 and corretto:
        print(True)
        corretto=False
if corretto==True:
    print(False)
        
    
    
