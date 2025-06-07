import re 
def Ex2(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    with open(file, encoding='UTF=8') as txt:
        txt=txt.read()
        #pattern=r'\b(\w)\w*(\w)\b\W*\b\2\w*\1\b'
        pattern=r'\b\w*(\w)\w*(\w)\w*\b\W*\b\w*\2\w*\1\w*\b'
    #   pattern=r'\b\w*(\w)\w*(\w)\w*\b\W*\b\w*\2\w*\1\w*\b'

        test=re.finditer(pattern,txt, flags=re.IGNORECASE)
        result=0
        for tester in test:
            print(tester)
            result+=1
        print(result)
        print(test)
        return result   
###############################################################################

if __name__ == '__main__':
    from tester import tester_fun
    import re

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex2, ["file2_1.txt"] , 3)
    counter_test_positivi += tester_fun(Ex2, ["file2_2.txt"] , 6)
    counter_test_positivi += tester_fun(Ex2, ["file2_3.txt"] , 8)
    counter_test_positivi += tester_fun(Ex2, ["file2_4.txt"] , 9)
    counter_test_positivi += tester_fun(Ex2, ["file2_5.txt"] , 11)
    
    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
