str1 = input('Inserire una stringa : ')

distanza = 0
for i in range(0,len(str1)):
    caratt = str1[i]
    for c in range(i + 1,len(str1)):
        if(str1[c] == caratt):
            print('Congtrolll carattere : ' + caratt + ' distanza = ' + str(c - i))
            if((c - i) > distanza):
                distanza = c - i

print('La distanza maggiore tra due lettere uguali nella stringa è : ' + str(distanza))
