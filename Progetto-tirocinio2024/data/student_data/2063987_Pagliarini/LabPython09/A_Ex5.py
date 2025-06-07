def A_Ex5(filename,oggetto):
    f=open(filename,encoding='UTF-8')
    t=f.readline()
    t=t.strip().split(',')
    n=1
    l=[]
    mx=0
    for el in f:
        if oggetto in el:
            el=el.strip().split(',')
            for i in el:
                if i.isdigit():
                    l.append(int(i))
            for k in range(len(l)-1):
                    if l[k+1]-l[k]>=mx:
                        n=k+2
                        mx= l[k+1]-l[k]
    return int(t[n])
                    
                        
                        
            
        
    
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex5, ['Vendite1.csv','Giubbotto'] , 2012)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite1.csv','Zaino'] , 2010)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite2.csv','Maglione'] , 2012)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite2.csv','Zaino'] , 2013)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite3.csv','Giubbotto'] , 2013)

    print('La funzione',A_Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
