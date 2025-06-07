def A_Ex4(filename,anno):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    
    f=open(filename,encoding='UTF-8')
    annata=f.readline().strip().split(',')
    x=0
    y=''
    for an in range(len(annata)):
        if annata[an].isdecimal() and int(annata[an])==anno:
            i=an
    for riga in f:
        oggetto=riga.strip().split(',')
        if int(oggetto[i])>x:
            x=int(oggetto[i])
            y=oggetto[0]
        elif int(oggetto[i])==x:
            if max[oggetto[0],y]==oggetto[0]:
                x=int(oggetto[i])
                y=oggetto[0]
    f.close()
    return y
     
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
