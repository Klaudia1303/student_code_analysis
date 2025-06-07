def A_Ex4(filename,anno):
    fin=open(filename,'r',encoding='UTF-8')
    s=fin.readline()
    s=s.strip().split(',')
    k=0
    ris=''
    conta=0
    for i in range(len(s)):
        k=(s[i])
        if str(k)==str(anno):
            break
    for riga in fin:
        riga=riga.strip().split(',')
        if int(riga[i])>int(conta):
            conta=riga[i]
            ris=riga[0]
        elif int(riga[i])==int(conta) and riga[0]>ris:
            ris=riga[0]
    return ris
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
     
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
