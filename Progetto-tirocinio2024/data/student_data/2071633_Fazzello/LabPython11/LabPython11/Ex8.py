def Ex8(file):
    import re
    l=[]
    d={'A':['01',31],'B':['02',28],'C':['03',31],'D':['04',30],'E':['05',31],'H':['06',30],'L':['07',31],'M':['08',31],'P':['09',30],'R':['10',31],'S':['11',30],'T':['12',31]}
    pttrn1=r'([A-Z]{3} ?[A-Z]{3} ?)(([0-9]{2})([A-Z])([0-9]{2}) ?)([A-Z][0-9]{3}[A-Z])'
    r=open(file,encoding='UTF-8').read().strip().split('\n')
    #print(r)
    for i in r:
        m=re.search(pttrn1,i)
        if  not m:
            l.append('Codice errato')
        else:
            if int(m.group(2)[3:5])<=d.get(m.group(2)[2])[1]:
                giorno=m.group(2)[3:5]
            mese=m.group(2)[2]
            #print(m.group(2)[3:5])
            elif m.group(2)[2] not in d.keys():
                l.append('Mese errato')
            else:
                if int(m.group(2)[3:5])>71:
                    l.append('Giorno errato')
                else:
                    
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
