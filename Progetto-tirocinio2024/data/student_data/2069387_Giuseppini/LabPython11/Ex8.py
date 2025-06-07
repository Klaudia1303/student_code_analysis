def Ex8(file):
    import re
    f=open(file, encoding='UTF-8')
    t=f.read()
    ris=[]
    pasqui=[]
    mesi= 'ABCDEHLMPRST'
    pattern=r'[A-Z]{3} ?[A-Z]{3} ?([0-9]{2})([A-T])([0-9]{2}) ?[A-Z][0-9]{3}[A-Z]'
    cod=re.finditer(pattern,t)
    tt=re.findall(pattern,t)
    t=t.split('\n')
    for elem in t:
        if elem in tt:
            for m in cod:
                aa=int(m.group(1))
                mm=m.group(2)
                gg=int(m.group(3))
                if aa<=20:
                    anno=2000+aa
                else:
                    anno=1900+aa
                if mm=='A':
                    mese='01'
                if mm=='B':
                    mese='02'
                if mm=='C':
                    mese='03'
                if mm=='D':
                    mese='04'
                if mm=='E':
                    mese='05'
                if mm=='H':
                    mese='06'
                if mm=='L':
                    mese='07'
                if mm=='M':
                    mese='08'
                if mm=='P':
                    mese='09'
                if mm=='R':
                    mese='10'
                if mm=='S':
                    mese='11'
                if mm=='T':
                    mese='12'
                if mm!='A' and mm!='B' and mm!='C' and mm!='D' and mm!='E' and mm!='H' and mm!='L' and mm!='M' and  mm!='P' and mm!='R' and mm!='S' and mm!='T':
                    ris=ris+['Mese Errato']
                    break
                if gg>40:
                    giorno= gg-40
                else:
                    giorno=gg
                    if giorno>31:
                        ris=ris+['Giorno Errato']
                        break
                data= str(giorno)+'/'+mese+'/'+str(anno)
                ris=ris+[data]
            else:
                ris=ris+['Codice Errato']

   
    return pasqui
    
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
