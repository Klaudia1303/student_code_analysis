def Ex6(file):
    fopen=open(file,'r',encoding='UTF-8')
    testo=fopen.read()
    fopen.close()
    pattern=r'\b(\w)\w*(\w)\2\w*\1\b'
    ris=re.finditer(pattern,testo,re.IGNORECASE)
    count=0
    for elem in ris:
        print(elem.group())
        count+=1
    return count
    
    
 
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
