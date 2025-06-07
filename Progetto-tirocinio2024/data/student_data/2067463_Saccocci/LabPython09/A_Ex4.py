def A_Ex4(filename,anno):
    f=open(filename,'r',encoding='UTF-8')
    l=[]
    for righe in f:
        l.append(righe.strip().split(','))
    f.close()
    anno1=0
    ogg=0
    ris=''
    for i in range(len(l[0])):
        if l[0][i]==str(anno):
            anno1=i
            break
    l.remove(l[0])
    for j in l:
        if int(j[anno1])>ogg or int(j[anno1])==ogg and j[0]>ris:
            ogg=int(j[anno1])
            ris=j[0]
    return ris
        
    
    
     
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
