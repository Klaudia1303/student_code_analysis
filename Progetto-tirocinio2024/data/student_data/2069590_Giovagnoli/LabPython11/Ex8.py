def Ex8(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    #Scrivere una funzione Python che prende in ingresso un file di testo contenente dei codici fiscali,
    #scritti uno per riga e che possono contenere o meno spazi tra i vari campi, e restituisce la lista (nell’ordine
    #in cui sono nel file) delle date di nascita nel formato dd/mm/aaaa (2 cifre obbligatorie per giorno e mese,
    #4 per anno). Si assuma che se l’anno xx nel codice fiscale è minore o uguale a 20 allora l’anno corrisponde
    #a 20xx, altrimenti corrisponde a 19xx.     ABC XYZ aaMgg WnnnV  (formato dei codici fiscali)
    #Dove ABC e XYZ sono sequenze di lettere MAIUSCOLE prese rispettivamente dal cognome e dal nome,
    #aa denota le ultime due cifre dell’anno, M è una lettera maiuscola che specifica il mese secondo la seguente
    #tabella riportata a lato, gg denota il giorno di nascita
    #con la regola che se è maggiore di 40 allora il sesso
    #è femminile e per calcolare la data corretta bisogna
    #togliere 40. L’ultima parte indica il codice del
    #comune (o stato estero) di nascita, composto da una
    #lettera maiuscola e 3 cifre, mentre l’ultima lettera
    #maiuscola è un carattere di controllo. I 4 campi
    #possono essere separati da spazi bianchi oppure
    #essere attaccati. Se la riga NON contiene un codice fiscale corretto dovete inserire nella lista la stringa
    #'Codice errato', se il codice del mese è inesistente allora inserite nella lista la stringa 'Mese errato', se il
    #giorno è scorretto allora inserite nella lista la stringa 'Giorno errato'. Nella verifica dei giorni potete ignorare
    #gli anni bisestili ed assumere che Febbraio abbia sempre 28 giorni.

    f=open(file,encoding="UTF-8")
    pattern=r'[A-Z]{3}\s?[A-Z]{3}\s?(\d{2})([A-Z])(\d{2})\s?\w[0-9]{3}\w'

    lista=[]
    d={}
    mesi='ABCDEHLMPRST'
    valori_mesi=['01','02','03','04','05','06','07','08','09','10','11','12']
    giorni_al_mese=[31,28,31,30,31,30,31,31,30,31,30,31]
    data=''

    i=0
    for x in mesi:
        d[x]=[valori_mesi[i],giorni_al_mese[i]]
        i+=1
#    print(d)

    for riga in f:
        ricerca=re.search(pattern,riga)

        if ricerca==None:
            lista.append('Codice errato')
        else:
            cf= ricerca.group()
            anno=ricerca.group(1)
            mese= ricerca.group(2)
            giorno=ricerca.group(3)

            #anno
            if int(anno)<=20:
                anno1='20'+str(anno)
            else:
                anno1='19'+str(anno) 
            #mese
            if mese not in d:
                lista.append('Mese errato')
                continue
            else:
                mese1=d[mese][0] 
            #giorno
            if int(giorno)>40:
                giorno1=int(giorno)-40
                if giorno1 not in range(1,d[mese][1]):
#                    print('mese: ',d[mese],' ',d[mese][1])
                    lista.append('Giorno errato')
                    continue
            elif 0<int(giorno)<=40:
                giorno1=int(giorno)
                if giorno1 not in range(1,d[mese][1]):
#                    print('mese: ',d[mese],' ',d[mese][1])
                    lista.append('Giorno errato')
                    continue
            #data
            if giorno1<10:
                giorno1='0'+str(giorno1)
            else:
                giorno1=str(giorno1)
            data=giorno1+'/'+mese1+'/'+anno1
            lista.append(data)

    f.close()            
    return lista

###############################################################################

if __name__ == '__main__':
    from tester import tester_fun
    import re

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex8, ["codici1.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato'])
    counter_test_positivi += tester_fun(Ex8, ["codici2.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato'])
    counter_test_positivi += tester_fun(Ex8, ["codici3.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921'])
    counter_test_positivi += tester_fun(Ex8, ["codici4.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921', '01/11/1931'])
    counter_test_positivi += tester_fun(Ex8, ["codici5.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921', '01/11/1931', 'Codice errato', 'Giorno errato'])

    print('La funzione',Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
