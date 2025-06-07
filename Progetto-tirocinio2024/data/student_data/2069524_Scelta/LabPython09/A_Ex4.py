def A_Ex4(filename,anno):
    f=open(filename,encoding='UTF_8')
    anni=f.readline().strip().split(',')
    colonna_anno=anni.index(str(anno))
    
    ogg_più_venduto=''
    vendite=0
    
    for line in f.readlines():
        data=line.strip().split(',')
        vendita_richiesta=int(data[colonna_anno])
        if vendita_richiesta>vendite:
            ogg_più_venduto=data[0]
            vendite=vendita_richiesta
        elif vendita_richiesta==vendite:
            ogg_più_venduto=max(data[0],ogg_più_venduto)
            
    return ogg_più_venduto
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
