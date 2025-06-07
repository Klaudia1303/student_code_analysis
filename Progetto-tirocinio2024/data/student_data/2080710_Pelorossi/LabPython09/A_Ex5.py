def A_Ex5(filename,oggetto):
    l=[]
    l1=[]
    l2=[]
    l3=[]
    f=open(filename, encoding='UTF-8')

    for riga in f:
        l.append(riga)
    for i in range(len(l)):
        riga=l[i].strip().split(',')
        l1.append(riga)
    for i in range(len(l1)):
        if oggetto in l1[i]:
            l2.append(l1[i])
            for j in l1[i]:
                if j.isalpha():
                    0
                else:
                    l3.append(j)
    return int(l1[0][l3.index(max(l3))+1])




    
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
