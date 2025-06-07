def A_Ex4(filename,anno):
    f=open(filename,encoding="UTF-8")
    l=[]
    for elem in f:
        elem=elem.strip().split(",")
        l.append(elem)
    for i in range(len(l[0])):
        if l[0][i]==str(anno):
            ann=i
            break
    count=0
    prodmax=''
    for i in range(1,len(l)):
        if int(l[i][ann])>count:
            count=int(l[i][ann])
            prodmax=l[i][0]
        elif int(l[i][ann])==count and l[i][0]>prodmax:
            prodmax=l[i][0]
    return prodmax
        
     
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
