def A_Ex4(filename,anno):
    f=open(filename,encoding="UTF-8")
    sv=[]
    Max=0
    prodotto=''
    colonna=0

    for elem in f:
        elem=elem.strip().split(",")
        sv.append(elem)

    for i in range(1,len(sv[0])):
        numero_anno=int(anno)
        if int(sv[0][i])==numero_anno:
            break
    colonna=i

    
    for k in range(1,len(sv)):
        if int(sv[k][colonna])>Max:
               Max=int(sv[k][colonna])
               prodotto=(sv[k][0])
        if int(sv[k][colonna])==Max:
            if ord(prodotto[0])>ord(sv[k][colonna][0]):
                prodotto=prodotto
            elif ord(prodotto[0])<ord(sv[k][colonna][0]):
                prodotto=sv[k][0]
                
               
    
    f.close()
    return prodotto



    

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
