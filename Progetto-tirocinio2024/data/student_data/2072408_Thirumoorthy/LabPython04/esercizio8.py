s=input('inserisci i dati di ingresso')
a=input('inserisci i dati di ingresso')
while s[len(s)-1]!=a[0]:
    s=a
    a=input('inserisci i dati di ingresso') 
    
print(s,a)
    
