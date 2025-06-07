def A_Ex8(fileName):
    rigamax=0
    riga=0

    f=open(fileName,encoding='UTF-8')
    x=f.readlines()
    for i in range(len(x)):
        maiuscole=0
        for lettera in range(len(x[i])):
            if ord(x[i][lettera])>64 and ord(x[i][lettera])<91:
                maiuscole+=1
            if maiuscole>=rigamax:
                rigamax=maiuscole
                riga=i+1
    f.close()
                    
    return riga
                     
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
