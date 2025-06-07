s=input("Inserisci stringa alfanumerica: ")
Max=1
carattere=s[len(s)-1]
acc=1
for i in range(1,len(s)): 
    if s[i]==s[i-1]:
        acc+=1
        if acc>=Max:
            Max=acc
            carattere=s[i]
    else:
        acc=1
print(carattere, Max)

       
            
