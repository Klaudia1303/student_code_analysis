def A_Ex8(fileName):
    f=open(filename,encoding='UTF–8')
    s=f.readline()
    r_max=0
    riga_max=0
    for i in range(len(s)):
        maiuscol=0
        for j in range(len(s[i])):
            if ord(s[i][j])>64 and ord(s[i][j])<91:
                   maiuscol+=1
            if maiuscol>=r_max:
                   r_max=maiuscol
                   riga_max=i+1
    return riga_max












    
 
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
