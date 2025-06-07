def A_Ex4(filename,anno):
    f=open(filename,'r',encoding="UTF-8")
    lfile=[]
    risultato="Non è presente l'anno"
    for el in f:
        l=el.split(',')
        for c in range(len(l)):
            l[c]=l[c].strip()
        lfile.append(l)
    for i in range(len(lfile)):
        for j in range(len(lfile[i])):
            if not lfile[i][j].isalpha(): 
                if int(lfile[i][j])==anno:
                    valore=0
                    risultato=""
                    for k in range(1,len(lfile)):
                        if valore<int(lfile[k][j]):
                            valore=int(lfile[k][j])
                            risultato=lfile[k][0]
    return risultato
    
            
     
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
