def Ex3(file):
    c=0
    f=open(file,encoding="UTF-8")
    pattern= r'\b\w*?(\w){2}\w*?\b\W*\b\w*?\1{2}\w*?\b\W*\b\w*?\1{2}\w*\b'
    for line in f:
        m=re.search(pattern, line,re.IGNORECASE)
        i=re.finditer(pattern, line,re.IGNORECASE)
        for m in i:
            if m:
                c+=1
    return c
        
        
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
