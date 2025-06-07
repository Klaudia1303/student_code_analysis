def Ex1(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
import re 
def Ex1(file):
    with open(file, encoding='UTF=8') as txt:
        txt=txt.read()
        pattern=r'\b(\w)\w*(\w)\b\W*\b\1\w*\2\b'
        test=re.finditer(pattern,txt, flags=re.IGNORECASE)
        result=0
        for tester in test:
            print(tester)
            result+=1
        print(result)
    return result    
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
