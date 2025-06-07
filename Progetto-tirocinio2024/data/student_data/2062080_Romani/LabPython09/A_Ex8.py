def A_Ex8(fileName):
    f=open(fileName, encoding='UTF-8')
    max_num = 0
    riga = 0
    for idx, line in enumerate(f.readlines()):
         num = 0
         for ch in line:
            if ch.isalpha() and ch.isupper():
                  num += 1

         if num > max_num:
              max_num = num
              riga = idx + 1
         if num == max_num:
              riga = max(riga, idx + 1)

    return riga
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
