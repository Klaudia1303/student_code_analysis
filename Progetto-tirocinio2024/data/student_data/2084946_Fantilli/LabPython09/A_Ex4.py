def A_Ex4(fileName,anno):
    f=open(fileName,encoding="UTF-8")
    intestazione=f.readline().strip().split(',')
    posizione=0
    max=0
    oggetto=''
    for i in range(len(intestazione)):
        if intestazione[i].isdecimal() and int(intestazione[i])==anno:
            posizione=i
    for j in f:
        hype=j.strip().split(',')
        if int(hype[posizione])>max or int(hype[posizione])==max and hype[0]>oggetto:
            max=int(hype[posizione])
            oggetto=hype[0]
    f.close()
    return oggetto
    
     
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
