def A_Ex4(filename,anno):
    numero=0
    f=open(filename,  encoding="UTF-8")
    riga=f.readline()
    lanni=riga.strip().split(",")
    anno=str(anno)
    if anno in lanni:
        pos=lanni.index(anno)
        for riga in f:
            elem=riga.strip().split(",")
            vendite=elem[pos]
            vendite=int(vendite)
            if vendite>numero:
                oggetto=elem[0]
                numero=vendite
        oggetto=str(oggetto)
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
