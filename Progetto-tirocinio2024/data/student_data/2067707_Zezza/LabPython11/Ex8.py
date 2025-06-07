def Ex8(file):
    l=[]
    mesi='ABCDEHLMPRST'
    f=open(file,encoding='UTF-8')
    pattern=r'\b[A-Z]{3}\W*[A-Z]{3}\W*(\d\d)([A-Z])(\d\d)\W*([A-Z]\d\d\d)([A-Z])\b'
    for riga in f:
        m=re.search(pattern,riga)
        if m==None:                                         #verifica codice
            data='Codice errato'
        else:
            data='ok'
            if int(m.group(1))<=20:                         #verifica anno
                anno='20'+m.group(1)
            else:
                anno='19'+m.group(1)
            k=0
            if m.group(2) in mesi:                          #verifica mese
                for i in mesi:
                    k+=1
                    if i==m.group(2) and k<10:
                        mese='0'+str(k)
                    elif i==m.group(2) and k>9:
                        mese=str(k)
            else:
                data='Mese errato'
            if 72>int(m.group(3))>49:                       #verifica giorno
                giorno=str(int(m.group(3))-40)
            elif 50>int(m.group(3))>40:
                giorno='0'+str(int(m.group(3))-40)
            elif 0<int(m.group(3))<32:
                giorno=m.group(3)
            else:
                data='Giorno errato'
            if mese=='02' and int(giorno)>28:               #verifica giorno/mese
                data='Giorno errato'
            if mese in '04 06 09 11' and giorno=='31':
                data='Giorno errato'    
            if data=='ok':                                  #data
                data=giorno+'/'+mese+'/'+anno
        l.append(data)
    return l
            
    
    
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
