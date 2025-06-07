def A_Ex8(fileName):
    with open(fileName, encoding="UTF-8") as f:
        t = f.readlines()
        i = 0
        maxCount = 0
        maxCountRow = 0
        while i < len(t):
            currCount = 0
            for c in t[i].split():
                if c.isupper():
                    currCount += 1
            if currCount >= maxCount:
                maxCount = currCount
                maxCountRow = i
            i += 1
    return maxCountRow + 1
 
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
