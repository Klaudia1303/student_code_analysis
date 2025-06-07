
s1 = input('Inserire una stringa: ')
s2 = input('Inserire la seconda stringa: ')
sem = False
sequenza = ''
temp = ''
posizione = -1
maxOcc = ''
# prendi un carattere
# se questo è trovato nella seconda stringa
# allora abbiamo una partenza e usciamo e un carattere
#altrimenti niente

# prendiamo un altro carattere
# se lo troviamo dopo la partenza allora prendiammo il carattere e una nuova partenza 
# se non trovato si ha partenza = 0 

#casaletto
#salerno
# a presa
# s presa
# allbabbajj
# perlabba
index = 0
posizione = -1
for i in  range (0, len(s1)):
    carattereS1 = s1[i]
    if(s2.count(carattereS1) > 1):
        index = s2.find(carattereS1)
    else:
        index = s2.find(carattereS1)
    if(index > -1):
        cont = 0
        print('Faccio per il caratt: ' + carattereS1 + ' index:' + str(index),end='\n')
        for c in range(index, len(s2)):
            if((i + cont) < len(s1)):
                if(s2[c] == s1[i + cont]):
                    cont += 1
                    temp += s2[c] 
                    #print('Aggiungo :' + s2[c] + ' per il controllo di ' + carattereS1)

                else:
                    #print(temp,end='\n')
                    if(len(temp) > len(maxOcc)):
                        maxOcc = temp
                    temp = ''
                    break
                if(c == len(s2) - 1 and len(maxOcc) < len(temp)):
                        maxOcc = temp
                        temp = ''
            else:
                if(len(temp) > len(maxOcc)):
                    maxOcc = temp
                    temp = ''
            
        else:
            continue  
        print('----------------------')      
                    


          

print(maxOcc)