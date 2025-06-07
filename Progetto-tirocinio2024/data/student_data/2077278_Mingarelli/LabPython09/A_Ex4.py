def A_Ex4(filename,anno):
    f=open(filename,encoding='UTF-8')
    riga=f.readline()
    elementi=f.readlines()
    magg=0
    num=0
    anni=riga.replace(',',' ').split()
    
    for i in anni[1:]:
        if int(i)==anno:
            num=anni.index(i)
            
    for elem in elementi:
        elem=elem.strip().split(',')
        if int(elem[num])>magg:
            magg=int(elem[num])
            piuvenduto=elem[0]
            
        elif int(elem[num])==magg:
            if elem[0]>piuvenduto:
                magg=int(elem[num])
                piuvenduto=elem[0]
                
    return piuvenduto
            
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
