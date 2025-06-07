def A_Ex4(filename,anno):
    fin=open(filename,encoding="UTF-8")
    oggmax=''
    vendmax=0
    righe=fin.readlines()
    fin.close()
    Dati=righe[0].strip().split(",")
    
    for j in range(len(Dati)):
        if Dati[j].isdecimal():
            Dati[j]=int(Dati[j])
            
    pos=Dati.index(anno)
    for i in range(1,len(righe)):
        r=righe[i].strip().split(",")
        if int(r[pos])>vendmax:
            vendmax=int(r[pos])
            oggmax=r[0]
        elif int(r[pos]) == vendmax:
            if r[0]>oggmax:
                vendmax=int(r[pos])
                oggmax=r[0]
            
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
