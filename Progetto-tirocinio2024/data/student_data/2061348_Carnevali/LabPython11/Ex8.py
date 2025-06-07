def Ex8(file):
    f=open(file, 'r', encoding='UTF-8')
    l=[]
    d={'A':'01','B':'02','C':'03','D':'04','E':'05','H':'06','L':'07','M':'08','P':'09','R':'10','S':'11','T':'12'}
    t=['11', '04', '06', '09']
    for c in f:
        p=''
        for k in c:
            if k.isalpha() or k.isdecimal():
                p+=k
        if len(p)==16 and p[15].isalpha():
            n=p[:6]
            if int(p[6:8])<=20:
                a=2000+int(p[6:8])
            elif int(p[6:8])>20:
                a=1900+int(p[6:8])
            if p[8] in d:
                m=d.get(p[8])
                if int(p[9:11])>40:
                    g=int(p[9:11])-40
                    if g<10:
                        g='0'+str(g)
                else:
                    g=p[9:11]
                if int(g)>31 or int(g)>30 and m in t or int(g)>28 and m=='02':
                    rest='Giorno errato'
                else:
                    rest=str(g)+'/'+str(m)+'/'+str(a)
            else:
                rest='Mese errato'
        else:
            rest='Codice errato'
        l.append(rest)
    return l
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
