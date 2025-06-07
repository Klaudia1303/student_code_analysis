def Ex8(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f=open(file)
    dl=[]
    dm={'A':'01','B':'02','C':'03','D':'04',\
        'E':'05','H':'06','L':'07','M':'08',\
        'P':'09','R':'10','S':'11','T':'12'}
    for l in f:
        p='[A-Z]{3}[ ]*[A-Z]{3}[ ]*([0-9]{2})[ ]*([A-Z])[ ]*([0-9]{2})[ ]*[A-Z][ ]*[0-9]{3}[ ]*[A-Z][ ]*'
        a=re.search(p,l)
        if a:
            month=a.group(2)
            if month in dm:
                month=dm[month]
                day=int(a.group(3))
                if day>=40:
                    day-=40
                if day<=31 and day>=1 and month in ['01','03','05','07','08','10','12']\
                   or day<=30 and day>=1 and month in ['04','06','09','11']\
                   or day<=28 and day>=1 and month=='02':
                    if day<10:
                        day='0'+str(day)
                    else:
                        day=str(day)
                    year=int(a.group(1))
                    if year>20:
                        year+=1900
                    elif year<21:
                        year+=2000
                    s=day+'/'+month+'/'+str(year)
                    dl.append(s)
                else:
                    dl.append('Giorno errato')
            else:
                dl.append('Mese errato')
        else:
            dl.append('Codice errato')
        
    return dl

    
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
