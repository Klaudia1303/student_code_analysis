def Ex8(file):
    fi=open(file,'r',encoding='UTF-8')
    file=fi.readlines()
    lista=[]
    d={'A':'01','B':'02','C':'03','D':'04','E':'05','H':'06','L':'07','M':'08','P':'09','R':'10','S':'11','T':'12'}
    pattern=r'\b([A-Z]{3})\s?([A-Z]{3})\s?(\d{2})([A-Z])(\d{2})\s?([A-Z]\d{3}[A-Z])\b'
    for codice in file:
        ricerca=re.search(pattern,codice)
        if ricerca:
            if ricerca.group(4) in d.keys():
                mese=d[ricerca.group(4)]
            else:
                mese=('Mese errato')
            if int(ricerca.group(5))>40:
                giorno=int(ricerca.group(5))-40
            else:
                giorno=int(ricerca.group(5))
            if int(ricerca.group(3))<=20:
                anno='20'+ricerca.group(3)
            else:
                anno='19'+ricerca.group(3)
            if mese!='Mese errato':
                if mese=='02' and giorno>28:
                    lista.append('Giorno errato')
                elif (mese=='11' or mese=='09' or mese=='04' or mese=='06') and giorno>30:
                    lista.append('Giorno errato')
                elif (mese=='01' or mese=='07' or mese=='03' or mese=='05' or mese=='07' or mese=='08' or mese=='10' or mese=='12') and giorno>31:
                    lista.append('Giorno errato')
                else:
                    if giorno<10:
                        giorno='0'+str(giorno)
                    data=str(giorno)+'/'+mese+'/'+str(anno)
                    lista.append(data)
            else:
                lista.append('Mese errato')
        else:
            lista.append('Codice errato')
    return lista
                                                                       
            







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
