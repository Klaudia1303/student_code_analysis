def A_Ex5(fileName,oggetto):
    f=open(fileName,encoding="UTF-8")
    max=0
    intestazione=f.readline().strip().split(',')
    scelta=f.readline().strip().split(',')
    a=True
    anno=int(intestazione[1])
    while a:
        if scelta[0]!=oggetto:
            scelta=f.readline().strip().split(',')
        elif scelta[0]==oggetto:
            for i in range(1,len(scelta)-1):
                crescita=int(scelta[i+1])-int(scelta[i])
                if crescita>=max:
                    max=crescita
                    anno=int(intestazione[i+1])
            break
    f.close()
    return anno

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
