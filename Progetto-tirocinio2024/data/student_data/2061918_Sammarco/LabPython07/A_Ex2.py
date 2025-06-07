def A_Ex2(start,n):
    l3=[]
    if n==0:
        l3=[]
    for i in range(n):
        if i!=0:
            start+=2
        if start%2!=0:
            l3.append(start)
        if start%2==0:
            start=start+1
            l3.append(start)
    return l3
s=A_Ex2
print(s)

        
       
                
        
    

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex2, [4,3], [5,7,9])
    counter_test_positivi += tester_fun(A_Ex2, [15,3], [15,17,19])
    counter_test_positivi += tester_fun(A_Ex2, [15,0], [])
    counter_test_positivi += tester_fun(A_Ex2, [0,3], [1,3,5])
    counter_test_positivi += tester_fun(A_Ex2, [201,1], [201])

    print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
