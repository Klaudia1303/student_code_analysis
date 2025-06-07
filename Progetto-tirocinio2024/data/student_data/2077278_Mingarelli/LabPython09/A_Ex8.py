def A_Ex8(fileName):
    file=open(fileName,encoding='UTF-8')
    mass=0
    c=0
    maxalpha=0
    for riga in file:
        c+=1
        
        alpha=0
        for j in riga:
            if j>='A' and j<='Z':
                alpha+=1
            if alpha>=maxalpha:
                maxalpha=alpha
                mass=len(riga)
                best=c

    return best
 
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
