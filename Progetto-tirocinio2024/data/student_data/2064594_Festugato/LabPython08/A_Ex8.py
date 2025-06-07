def A_Ex8(l):
    risultato = set()
    numeri = set()
    for i in l:
        for n in i:
            numeri.add(n)#insieme di numeri
    
    #print(numeri)
    volte = 0
  

    for n in numeri:
        for indice in range(len(l)):
           
            if n in l[indice]:
                #print(n,'inidice',indice,l[indice])
                volte += 1
                valore = n
                #print('occ',volte)
              
                
        if volte==1:
            risultato.add(valore)
        volte = 0

    return risultato
            
                
                
                
            
    
    
















    

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex8, [[{3,2,90},{2,87,23},{2,23,3}]] , {90,87})
    counter_test_positivi += tester_fun(A_Ex8, [[set(),{-10},{2}]] , {-10,2})
    counter_test_positivi += tester_fun(A_Ex8, [[set()]] , set())
    counter_test_positivi += tester_fun(A_Ex8, [[set(),{10,-2},{10},{-2}]] , set())
    counter_test_positivi += tester_fun(A_Ex8, [[set(),{10,-9,4},{4,-5,2},{3,7,4}]] , {10,-9,-5,2,3,7})


    print('La funzione',A_Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
