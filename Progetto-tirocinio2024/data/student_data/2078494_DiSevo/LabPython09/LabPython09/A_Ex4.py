def A_Ex4(filename,anno):
    f=open(filename,encoding='UTF-8')
    s=f.read()
    f.close()
    sol=[]
    solmax=0
    oggmax=''
    aa=0
    sp=s.split('\n')
    print(anno)
    for i in range(len(sp)):
        ris=[]
        ssp=sp[i].replace('\n',',')
        ris=ssp.split(',')
        if i==0:
            print(ris)
            for a in range(1,len(ris[i])):
                if ris[a]==str(anno):
                    print('test2')
                    aa=a
                    print(a,anno)
        else:
            sol.append((ris[0],ris[aa]))

    for j in range(len(sol)):
        if sol[j][1]>str(solmax):
            solmax=sol[j][1]
            oggmax=sol[j][0]
    return oggmax
     
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
