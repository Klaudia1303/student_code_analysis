
def A_Ex7(l):
    i = 0
    while i < (len(l) - 1):
        diff = l[i + 1] - l[i]
        if diff > 0:
            l.append(diff)
        i += 1

    return l
        



























# def A_Ex7(l):
#    l1 = []
#    l2 = []
#    for i in range(len(l) - 1):
#        if l[i + 1] > l[i]:
#            diff1 = l[i+1] - l[i]
#            l1.append(diff1)

#   print(l1)
    
 #   l1.extend(l)
  #  l2.extend(l1)
   # print(l2)
    
    #for i in range(len(l2) - 1):
     #   if l2[i + 1] > l2[i]:
      #      diff2 = l2[i+1] - l2[i]
       #     l2.append(diff2)
            

   # return l2







###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""    
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex7, [[10,1,11,31,251]] , [10,1,11,31,251,10,20,220,10,200,190])
    counter_test_positivi += tester_fun(A_Ex7, [[]] , [])
    counter_test_positivi += tester_fun(A_Ex7, [[2,7,3]] , [2,7,3,5,2])
    counter_test_positivi += tester_fun(A_Ex7, [[200,501,300]] , [200,501,300,301,1])
    counter_test_positivi += tester_fun(A_Ex7, [[3,2,0]] , [3,2,0])


    print('La funzione',A_Ex7.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
