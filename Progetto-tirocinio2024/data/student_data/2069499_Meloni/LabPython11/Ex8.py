def Ex8(file):
    testo=open(file,encoding='UTF-8')
    testo=testo.read().splitlines()
    
    diz={'A':'01','B':'02','C':'03','D':'04','E':'05','H':'06','L':'07','M':'08','P':'09','R':'10','S':'11','T':'12'}
    pattern=r'[A-Z]{3} ?[A-Z]{3} ?([0-9]{2})([A-Z])([0-9]{2}) ?[A-Z][0-9]{3}[A-Z]'
    mesi=["B","DHPS","ACELMRT"]
    intervallo=[(1,28),(1,30),(1,31)]
    lista=[]
    
    for codice_fiscale in testo:
        if re.match(pattern,codice_fiscale):
            anno=re.match(pattern,codice_fiscale).group(1)
            mese=re.match(pattern,codice_fiscale).group(2)
            giorno=int(re.match(pattern,codice_fiscale).group(3))
            x = ''
            if giorno>=41 and giorno<=71:
                giorno-=40
            c = 0
            for j in range(3):
                if mese in mesi[j]:
                    c = 1
                    if giorno in range(intervallo[j][0],intervallo[j][1]):
                        x += str(giorno).zfill(2)+'/'+diz.get(mese)+'/'
                        if int(anno) <= 20:
                            x += "20"+str(anno)
                        else:
                            x += "19"+str(anno)
                        lista.append(x)
                    else:
                        lista.append("Giorno errato")
            if c==0:
                    lista.append("Mese errato")
        else:
            lista.append("Codice errato")
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
