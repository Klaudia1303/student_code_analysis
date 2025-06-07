import re 
def Ex3(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    with open(file, encoding='UTF=8') as txt:
        txt=txt.read()
        pattern=r'\b\w*(\w)\1\w*\b\W\s*\b\w*\1\1\w*\b\W\s*\b\w*\1\1\w*\b\W*'

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

    counter_test_positivi += tester_fun(Ex3, ["file2_1.txt"] , 1)
    counter_test_positivi += tester_fun(Ex3, ["file2_2.txt"] , 2)
    counter_test_positivi += tester_fun(Ex3, ["file2_3.txt"] , 3)
    counter_test_positivi += tester_fun(Ex3, ["file2_4.txt"] , 4)
    counter_test_positivi += tester_fun(Ex3, ["file2_5.txt"] , 5)

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
