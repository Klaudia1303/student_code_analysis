def A_Ex4(filename,anno):
    a=open(filename, encoding="UTF-8")
    sv=[]
    y=0
    t=0
    for elem in a:
        elem=elem.strip().split(",")
        sv.append(elem)
    x=sv[0].index(str(anno))
    for i in range(1,len(sv)):
        if int(sv[i][x])>y:
            y=int(sv[i][x])
            nome=sv[i][0]
        elif int(sv[i][x])==y:
            if nome>(sv[i][0]):
                continue
            else:
                nome=sv[i][0]
    return nome
    
        
    
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
