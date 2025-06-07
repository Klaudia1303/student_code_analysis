def A_Ex4(fileName,anno):

    f=open(fileName,encoding="UTF-8")
    ls=[]
    a=0
    h=''
    d=0
    for i in f:
        i=i.strip().split(",")
        ls.append(i)
    for j in range(1,len(ls[0])):
        if int(ls[0][j])==int(anno):
            d=int(j)
            break
    for g in range(1,len(ls)):
        if int(ls[g][d])>=a:
            if len(h)==0:
                a=int(ls[g][d])
                h=ls[g][0]
            elif ord(ls[g][d][0])>ord(h[0]) and int(ls[g][d])==a:
                a=int(ls[g][d])
                h=ls[g][0]
            elif int(ls[g][d])>a:
                a=int(ls[g][d])
                h=ls[g][0]
                
                    
    f.close()
    return h
     
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
