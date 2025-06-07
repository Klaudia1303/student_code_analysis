def A_Ex4(filename,anno):
    f=open(filename, encoding='UTF-8')
    s=''
    z=0
    mas=0
    for riga in f:
        riga=riga.strip().split(',')
        if str(anno) in riga:
            z=riga.index(str(anno))
            continue
        if int(riga[z])>mas:
            mas=int(riga[z])
            s=riga[0]
        if riga[0]==mas:
            if riga[0]>s:
                s=riga[0]
    f.close
    return s
            
     
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
