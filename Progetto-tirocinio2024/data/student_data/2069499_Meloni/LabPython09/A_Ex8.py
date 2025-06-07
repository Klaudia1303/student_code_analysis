def A_Ex8(fileName):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    fin=open(fileName,encoding="UTF-8")
    s_tot=[]
    count=0
    max_count=0
    for elem in fin:
        elem=elem.strip().split('/n')
        s_tot.append(elem)
    fin.close()
    for i in s_tot:
        for j in i:
            if j.isupper():
                count+=1
        if count>=max_count:
            max_count=count
            max_index=s_tot.index(i)+1
        count=0
        
    return(max_index)
 
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex8, ["file1.txt"] , 2)
    counter_test_positivi += tester_fun(A_Ex8, ["file2.txt"] , 2)
    counter_test_positivi += tester_fun(A_Ex8, ["file3.txt"] , 2)
    counter_test_positivi += tester_fun(A_Ex8, ["file4.txt"] , 3)
    counter_test_positivi += tester_fun(A_Ex8, ["file5.txt"] , 3)

    print('La funzione',A_Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
