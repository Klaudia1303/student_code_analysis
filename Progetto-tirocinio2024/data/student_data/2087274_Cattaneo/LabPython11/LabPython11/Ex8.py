def Ex8(file):
    f=open(file,'r',encoding='UTF-8')
    pattern='[A-Z]{3} ?[A-Z]{3} ?([0-9]{2})([A-Z])([0-9]{2}) ?[A-Z][0-9]{3}[A-Z]'
    lista=[]
    for line in f:
        m=re.search(pattern,line)
        codice_errato=False
        mese_errato=False
        giorno_errato=False
        if m:
            if line.strip()==m.group():
                if int(m.group(3))>40:
                    giorno=int(m.group(3))-40
                else:
                    giorno=int(m.group(3))
                if m.group(2) in 'ABCDEHLMPRST':
                    if m.group(2) in 'ABCDE':
                        mese=ord(m.group(2))-64
                    elif m.group(2)=='H':
                        mese=6
                    elif m.group(2) in 'LM':
                        mese=ord(m.group(2))-69
                    elif m.group(2)=='P':
                        mese=9
                    else:
                        mese=ord(m.group(2))-72
                else:
                    mese_errato=True
                if giorno>31 or (giorno>30 and mese in [4,6,9,11]) or (giorno>28 and mese==2):
                    giorno_errato=True
            else:
                codice_errato=True
        if not m or codice_errato:
            lista.append('Codice errato')
        elif mese_errato:
            lista.append('Mese errato')
        elif giorno_errato:
            lista.append('Giorno errato')
        else:
            data=''
            if len(str(giorno))==1:
                   data+='0'+str(giorno)+'/'
            else:
                data+=str(giorno)+'/'
            if len(str(mese))==1:
                data+='0'+str(mese)+'/'
            else:
                data+=str(mese)+'/'
            if int(m.group(1))>20:
                data+='19'+m.group(1)
            else:
                data+='20'+m.group(1)
            lista.append(data)
    f.close()
    return lista          
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
