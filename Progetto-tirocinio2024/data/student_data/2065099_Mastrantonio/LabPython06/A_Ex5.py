s = input ('Inserisci una stringa alfanumerica: ')
contamax = 0
lett = s[0]
for i in range(len(s)-1):
    conta = 0 
    for j in range (i,len(s)):
        if s[i]==s[j]:
            conta = conta + 1
        else :
            break
    if contamax <= conta :
        contamax = conta
        lett = s [i]
print (lett, contamax)
