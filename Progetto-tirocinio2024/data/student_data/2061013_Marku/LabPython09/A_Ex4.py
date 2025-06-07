def A_Ex4(filename,anno):
    f=open(filename, encoding='UTF-8')
    pRiga=f.readline()
    anno=(pRiga.strip().split(',')).index(str(anno))
    lr=[]
    riga=f.readlines()
    for elem in riga:
        i=elem.strip().split(',')
        lr.append((i[0], i[anno]))
    massimo=0
    oggetto=''
    for j in lr:
        if int(j[1])>massimo:
            massimo=int(j[1])
            oggetto=j[0]
        elif int(j[1])==massimo and j[0]>oggetto:
            massimo=int(j[1])
            oggetto=j[0]
    f.close()
    return oggetto

    
    #"""MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
     
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex4, ['Vendite1.csv',2012] , 'Giubbotto')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite2.csv',2012] , 'Maglione')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite2.csv',2013] , 'Zaino')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite3.csv',2011] , 'Giubbotto')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite3.csv',2010] , 'Cellulare')
    
    print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
