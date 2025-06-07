def A_Ex5(filename,oggetto):
    fin=open(filename)
    L=[]
    m=0
    for riga in fin:
        riga=riga.strip().split(',')
        L.append(riga)
    best=L[0][1]
    for i in range(1,len(L)):
        if oggetto in L[i][0]:
            break
    for j in range(2,len(L[0])):
        if int(L[i][j])-int(L[i][j-1])>=m:
            m=int(L[i][j])-int(L[i][j-1])
            best=L[0][j]
    fin.close()        
    return int(best)               
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
