def A_Ex4(fileName,anno):
    f=open(fileName,encoding='UTF-8')
    vendite=0
    i=0
    for riga in f:
        riga=riga.strip().split(",")
        if str(anno) in riga:
            while riga[i]!=str(anno):
                i+=1
            x=i
        else:
            if int(riga[x])>vendite:
                vendite=int(riga[x])
                ogg=riga[0]
    f.close()       
    return ogg
                
            
            
            
        
                
        
     
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
