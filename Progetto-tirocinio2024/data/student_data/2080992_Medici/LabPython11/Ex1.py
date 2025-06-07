def Ex1(file):
    file=open(file, encoding='UTF-8')
    testo=file.read()
    print(testo)
    pattern= r'\b(\w)\w*(\w)\b\W*\b\1\w*\2\b'
    m=re.findall(pattern, testo, flags=re.IGNORECASE)
    file.close()
    return len(m)
###############################################################################

if __name__ == '__main__':
    from tester import tester_fun
    import re

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex1, ["file1_1.txt"] , 1)
    counter_test_positivi += tester_fun(Ex1, ["file1_2.txt"] , 2)
    counter_test_positivi += tester_fun(Ex1, ["file1_3.txt"] , 3)
    counter_test_positivi += tester_fun(Ex1, ["file1_4.txt"] , 3)
    counter_test_positivi += tester_fun(Ex1, ["file1_5.txt"] , 5)

    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
