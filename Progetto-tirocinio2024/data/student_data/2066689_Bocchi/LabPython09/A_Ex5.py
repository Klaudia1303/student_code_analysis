def A_Ex5(filename,oggetto):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    x=0
    ris=1
    crePrec=0
    crescita=0
    sv=[]
    f= open(filename,encoding='UTF-8')
    for el in f:
        el=el.strip().split(',')
        sv.append(el)
    while str(sv[x][0]) != str(oggetto):
        x +=1
    for b in range(1,len(sv[x])-1):
        if int(sv[x][b+1]) > int(sv[x][b]):
            crescita= int(sv[x][b+1]) - int(sv[x][b])
            if crescita >= crePrec:
                crePrec= crescita
                ris= b+1
    anno= int(sv[0][ris])
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
