def Ex3(file):
    s=open(file,encoding='UTF-8').read()
    m=re.finditer(r'\b\w*(\w)\1\w*[^\n][ ,]\w*\1\1\w*[^\n][ ,]\w*\1\1\w*\b',s,re.IGNORECASE)
    l=[]
    for match in m:
        l.append(match.group())
        print(match.group())
    return len(l)
    
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
