##Scrivere una funzione che prende in ingresso una lista l di insiemi di numeri interi e 
##restituisce un altro insieme contenente tutti e soli gli elementi che appaiono in uno ed uno solo degli 
##insiemi in l. Ad esempio, se x=[{3,2,90},{2,87,23},{2,23,3}], allora l'insieme da restituire sarà 
##{90,87}. Se la lista in ingresso è vuota, la funzione deve restituire un insieme vuoto

def A_Ex8(l):
    st=set()
    x=0
    for i in range(len(l)):
        l[i]=list(l[i])
        for j in range(len(l[i])):
            for k in range(len(l)):
                if l[i][j] in l[k] and i!=k:
                    x=x+1
            if x==0:
                st.add(l[i][j])
    x=0
    return st


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
