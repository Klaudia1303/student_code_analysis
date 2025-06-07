def A_Ex4(filename,anno):
    f=open(filename,encoding='UTF-8')
    s=f.readline()
    s=s.strip()
    s=s.split(',')
    colonna=0
    l=[]
    for i in range(1,len(s)):
        if int(s[i])==int(anno):
            colonna=i
    f.close()
    prodotto=str()
    precedente=0
    fin=open(filename,encoding='UTF-8')
    g=fin.readlines()
    fin.close()
    for k in g[1:]:
        k=k.split(',')
        if int(k[colonna])>precedente:
            precedente=int(k[colonna])
            prodotto=k[0]
        if int(k[colonna])==precedente:
            l.append(prodotto)
            l.append(k[0])
            l.sort()
            if l[0]==prodotto:
                precedente=int(k[colonna])
                prodotto=k[0]
            l.clear()
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
