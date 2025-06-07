s=input("inserisci stringa:")
carattere=""
massimo=1
count=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count+=1
        if count>=massimo:
            massimo=count
            carattere=s[i]
    else:
        count=1
print(carattere, massimo)
