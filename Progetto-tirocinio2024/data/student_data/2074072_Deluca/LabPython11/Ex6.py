def Ex6(file):
    f= open(file, encoding="UTF-8")
    s= " "+ f.read()+" "
    words=set()
    for i in range(97,123):
        for k in range(97, 123):
            pattern= r"\b"+ chr(i)+"\w*"+chr(k)*2+"\w*"+chr(i)+r"\b"
            m = re.findall(pattern, s, re.IGNORECASE)
            for elem in m:
                words.add(elem)
    return len(words)
 
###############################################################################

if __name__ == '__main__':
    from tester import tester_fun
    import re

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex6, ["file3_1.txt"] , 3)
    counter_test_positivi += tester_fun(Ex6, ["file3_2.txt"] , 3)
    counter_test_positivi += tester_fun(Ex6, ["file3_3.txt"] , 2)
    counter_test_positivi += tester_fun(Ex6, ["file3_4.txt"] , 4)
    counter_test_positivi += tester_fun(Ex6, ["file3_5.txt"] , 4)

    print('La funzione',Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
