def A_Ex5(filename,oggetto):
    f=open(filename, encoding='UTF-8')
    s=f.readline()
    sl=s.strip().split(',')
    s1=f.read()
    l=s1.strip().split('\n')
    c=0
    anno=''
    for ogg in l:
        ll=ogg.strip().split(',')
        if oggetto==ll[0]:
            for i in range(1,len(sl)-1):
                if int(ll[i+1])-int(ll[i])>=c:
                    c=int(ll[i+1])-int(ll[i])
                    anno=int(sl[i+1])
    
    return anno
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
