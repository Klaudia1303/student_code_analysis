def A_Ex8(fileName):
    f=open(fileName,'r',encoding='UTF-8')
    s=f.readlines()
    massch=0
    numriga=0

    for riga in range(len(s)):
        numch=0
        for j in range(len(s[riga])):
            if ord(s[riga][j])>64 and ord(s[riga][j])<91:
                numch+=1
            if numch>=massch:
                massch=numch
                numriga=riga+1
    f.close()
    
    return numriga
                    
 
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
 
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
