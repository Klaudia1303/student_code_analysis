def A_Ex4(filename,anno):
    f=open(filename,"r",encoding="UTF-8")
    riga=f.readline()
    anni=riga.strip().split(",")
    a=0
    stringa=""
    x=0
    for i in range(len(anni)):
        if str(anni[i])==str(anno):
            a=i
    while len(riga)>0:
        riga=f.readline()
        if len(riga)>0:
            dati=riga.strip().split(",")
            if int(dati[a])>x:
                stringa=dati[0]
                x=int(dati[a])
    f.close()
    return stringa
    
        
     
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
