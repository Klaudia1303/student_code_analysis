def Ex8(file):
    f=open(file,encoding='UTF-8')
    s=f.readlines()
    l=[]
    mesi=['A','B','C','D','E','H','L','M','P','R','S','T']
    pattern=r'^[A-Z]{3}\s*[A-Z]{3}\s*(\d{2})\s*([A-Z])\s*(\d{2})\s*[A-Z]\s*\d{3}\s*[A-Z]$'


    for riga in s:
        m=re.search(pattern,riga)

        if m:
            riga=riga.replace(' ','')
            year,month,day=int(m.group(1)),m.group(2),int(m.group(3))

            if year<=20:
                year+=2000
            elif year>20:
                year+=1900

            if month in mesi:
                month=str(mesi.index(month)+1).zfill(2)
            else:
                l.append('Mese errato')
                continue

            if day>40:
                day-=40
            if day>31 or day<1 or (day>28 and month=='02'):
                l.append('Giorno errato')
                continue

            l.append(str(day).zfill(2)+'/'+month+'/'+str(year))
    

        else:
            l.append('Codice errato')


    f.close()
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
