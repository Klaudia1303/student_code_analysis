def Ex8(file):
    f=open(file, encoding="UTF-8")
    lista=[]
    diz={}
    c=0
    MESI=['A','B','C','D','E','H','L','M','P','R','S','T']
    for i in MESI:
        c=c+1
        diz[i]=c
    pattern=r'\b([A-Z])([A-Z])([A-Z])\s*([A-Z])([A-Z])([A-Z])\s*([0-9])([0-9])\s*([A-Z])([0-9])([0-9])\s*([A-Z])([0-9])([0-9])([0-9])([A-Z])\b'
    for i in f:
        m=re.search(pattern, i)
        if m:
            anno=m.group(7)+m.group(8)
            if int(anno)<=20:
                anno=int('20'+anno)
            else:
                anno=int('19'+anno)
            mese=m.group(9)
            mese=str(diz.get(mese, 0))
            if int(mese)==0:
                lista.append('Mese errato')
                continue
            if len(mese)==1:
                mese=('0'+mese)
            giorno=int(m.group(10)+m.group(11))
            if (giorno)>40:
                giorno=(giorno)-40
            if len(str(giorno))==1:
                giorno='0'+str(giorno)
            if int(giorno)>31 and int(giorno)<41:
                lista.append('Giorno errato')
                continue
            if mese=='02' and int(giorno)>28:
                lista.append('Giorno errato')
                continue
            if (mese=='04' or mese=='06' or mese=='09' or mese=='11') and int(giorno)>31:
                lista.append('Giorno errato')
                continue
            data=str(giorno)+'/'+str(mese)+'/'+str(anno)
            lista.append(data)
        else:
            lista.append('Codice errato')
    return (lista)

    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    
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
