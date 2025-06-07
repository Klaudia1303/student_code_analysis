def A_Ex4(filename,anno):
    fin=open(filename,encoding='UTF-8')
    anni=fin.readline().strip().split(',')
    l=[]
    for i in fin:
        l.append(i.strip().split(','))
    fin.close()
    a=int(anno)-int(anni[1])+1
    M=l[0]
    for i in range(1,len(l)):
        if int(M[a])<int(l[i][a]):
            M=l[i]
        elif int(M[a])==int(l[i][a]) and len(M[0])<len(l[i][0]):
            M=l[i]
    return M[0]
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
