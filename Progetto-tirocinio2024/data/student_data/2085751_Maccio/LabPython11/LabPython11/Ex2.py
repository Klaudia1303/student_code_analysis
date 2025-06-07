def Ex2(file):
    fi=open(file,'r',encoding='UTF-8')
    fil=fi.read()
    a=re.findall(r'\b\w*(\w)\w*(\w)\w*\b\s\b\w*\2\w*\1\w*\b',fil,re.IGNORECASE)
    lun=len(a)
    return lun

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
