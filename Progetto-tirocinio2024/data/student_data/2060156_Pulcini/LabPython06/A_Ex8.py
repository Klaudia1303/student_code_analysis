s1=input('inserire la prima stringa:')
s2=input('inserire la seconda stringa:')
n=int(input('inserire un intero'))
risultato=''
for prima_ch in s1:
    for second_ch in s2:
        if prima_ch in s2 and (abs(s1.find(prima_ch)-s2.find(prima_ch))<=n):
            risultato+= prima_ch
            break
print(risultato)
