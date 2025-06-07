s1 = input ('Inserisci una stringa di testo: ')
s2 = input ('Inserisci una stringa di testo: ')
fine = ''
h= 0 
for i in range (len(s1)):
    sequenza = ''
    trova = s2.find(s1[i])
    if trova > 0 :
        for j in range (trova,len(s2)):
            h = h +1
            if s1[i+h]==s2[trova+h]:
                sequenza = sequenza + s2[trova+h]
            else :
                break
    if sequenza > fine:
        fine = sequenza
print(fine)
