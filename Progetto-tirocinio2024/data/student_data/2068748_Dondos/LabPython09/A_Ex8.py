def A_Ex8(fileName):
    f = open(fileName, "r", encoding="UTF-8")
    l = f.readlines()
    print(l)

    maxAlpha = 0
    maxLineIndex = 0
    lineIndex = 0

    for line in l:
        countAlpha = 0
        lineIndex += 1
        for c in line:
            if c.isupper():
                countAlpha += 1
            if countAlpha > maxAlpha:
                maxAlpha = countAlpha
                maxLineIndex = lineIndex
            elif countAlpha == maxAlpha:
                if lineIndex > maxLineIndex:
                    maxAlpha = countAlpha
                    maxLineIndex = lineIndex
    return maxLineIndex
            
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
