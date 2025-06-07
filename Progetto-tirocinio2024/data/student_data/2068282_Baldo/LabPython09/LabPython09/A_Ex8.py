def A_Ex8(fileName):
    f = open(fileName)
    s = f.readlines()
    f.close()

    maxx = 0
    Riga = 0

    for riga in range(len(s)):
        greater = 0
        for i in range(len(s[riga])):
            if ord(s[riga][i]) > 64 and ord(s[riga][i]) < 91:
                greater += 1
            if greater >= maxx:
                maxx = greater
                Riga = riga + 1
                
    return Riga
                

    
        
            
            
 
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
