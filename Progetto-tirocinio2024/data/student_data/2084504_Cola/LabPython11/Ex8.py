def Ex8(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f=open(file,encoding='UTF-8')
    s=f.readlines()
    d=s.copy()
    M='ABCDEHLMPRST'
    for i in range(len(s)):
        m=re.search(r'^[A-Z]{3}\s*[A-Z]{3}\s*(\d{2})\s*([A-Z])\s*(\d{2})\s*[A-Z]\s*\d{3}\s*[A-Z]$',s[i].strip())
        if m:
            anno,mese,giorno=m.group(1),m.group(2),int(m.group(3))
            if int(anno)<=20:
                ANNO='20'+anno
            elif int(anno)>20:
                ANNO='19'+anno
            if mese in M:
                if M.find(mese)+1<10:
                    MESE='0'+str(M.find(mese)+1)
                elif M.find(mese)+1>=10:
                    MESE=str(M.find(mese)+1)
                if giorno>40:
                    giorno=giorno-40
                if giorno<=31:
                    if mese in 'DHPS' and giorno>30:
                        d[i]='Giorno errato'
                        continue
                    elif mese in 'B' and giorno>28:
                        d[i]='Giorno errato'
                        continue
                    if giorno>=1 and giorno<=9:
                        giorno='0'+str(giorno)
                    d[i]=str(giorno)+'/'+MESE+'/'+ANNO
                else:
                    d[i]='Giorno errato'
            else:
                d[i]='Mese errato'
        else:
            d[i]='Codice errato'
    return d   
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

