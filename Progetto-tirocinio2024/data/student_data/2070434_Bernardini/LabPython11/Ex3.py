def Ex3(file):
    a=open(file,'r',encoding='UTF-8')
    x=0
    for riga in a:
        pattern=r'\b\w*(\w\w)\w*\b\W*\b\w*\1\w*\b\W*\b\w*\1\w*\b'
        z=re.findall(pattern, riga, flags=re.IGNORECASE)
        for n in z:
            x+=1
    return x
                                                               
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    
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
