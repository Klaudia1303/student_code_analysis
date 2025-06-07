def Ex6(file):
    testo=open(file,encoding="UTF-8").read()
    pattern= r'\b(\w)\w*(\w)\2\w*\1\b'
    num=re.findall(pattern,testo,re.IGNORECASE)
    ris=len(num)
    return ris
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
 
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
