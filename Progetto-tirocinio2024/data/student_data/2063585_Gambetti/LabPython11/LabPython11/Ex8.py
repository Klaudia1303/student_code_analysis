def Ex8(file):
    f=open(file,encoding='UTF-8')
    l=[]
    pattern=r'\b[A-Z]{3} ?[A-Z]{3} ?([0-9]{2})([A-Z])([0-9]{2}) ?[A-Z][0-9]{3}[A-Z]\b'
    for elem in f:
        m=re.match(pattern,elem)
        if m:
            a=m.group(1)
            if int(a)<=20:
                k='20'+a
            else:
                k='19'+a
            b=m.group(2)
            if b=='A':
                mese='01'
            elif b=='B':
                mese='02'
            elif b=='C':
                mese='03'
            elif b=='D':
                mese='04'
            elif b=='E':
                mese='05'
            elif b=='H':
                mese='06'
            elif b=='L':
                mese='07'
            elif b=='M':
                mese='08'
            elif b=='P':
                mese='09'
            elif b=='R':
                mese='10'
            elif b=='S':
                mese='11'
            elif b=='T':
                mese='12'
            else:
                l.append('Mese errato')
                continue 

            c=m.group(3)
            if int(c)>40:
                c=int(c)-40
            if len(str(c))==1:
                c='0'+str(c)
            if int(c)<=28 and b=='B':
                l.append(str(c)+'/'+mese+'/'+k)
            elif int(c)<=30 and b in 'SDHP':
                l.append(str(c)+'/'+mese+'/'+k)
            elif int(c)<=31 and b in 'ACELMRT':
                l.append(str(c)+'/'+mese+'/'+k)
            else:
                l.append('Giorno errato')
        else:
            l.append('Codice errato')
            continue
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
