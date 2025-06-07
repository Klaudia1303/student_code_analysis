s=input("Inserisci una stringa: ")
i=0
max=0
conta=0
posizione_max=0
j=''

while(i<len(s)):
    conta=s.count(s[i])
    
    if(conta>max):
        max=conta
        posizione_max=i
        carattere=s[i]
    elif(conta==max):
        if(i>posizione_max):
            posizione_max=i
            carattere=s[i]
    i+=1
    
print(carattere)
