def Ex3(file):
    f = open(file,encoding="UTF-8")
    l=f.readlines()
    count=0
    for elem in l:
        for i in range(97,123):
            pattern= (r"\b[a-z]*"+chr(i)*2+"[a-z]*"+"[^a-z]*")*2+"[a-z]*"+chr(i)*2+r"[a-z]*\b"
            m=re.findall(pattern, elem, re.IGNORECASE)
            count+=len(m)
    return count
    
###############################################################################

if __name__ == '__main__':
    from tester import tester_fun
    import re

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex3, ["file2_1.txt"] , 1)
    counter_test_positivi += tester_fun(Ex3, ["file2_2.txt"] , 2)
    counter_test_positivi += tester_fun(Ex3, ["file2_3.txt"] , 3)
    counter_test_positivi += tester_fun(Ex3, ["file2_4.txt"] , 4)
    counter_test_positivi += tester_fun(Ex3, ["file2_5.txt"] , 5)

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
