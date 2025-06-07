def A_Ex5(filename,oggetto):
    f=open(filename,encoding='UTF-8')
    riga=f.readline()
    anno=riga.strip().split(',')
    massimo=0
    a=anno[1]
    for elem in f:
        elem=elem.strip().split(',')
        if elem[0]==oggetto:
            for i in range(2,len(elem)):
                d=int(elem[i])-int(elem[i-1])
                if d>=massimo:
                    massimo=d
                    a=anno[i]
    return int(a)
                
    

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
