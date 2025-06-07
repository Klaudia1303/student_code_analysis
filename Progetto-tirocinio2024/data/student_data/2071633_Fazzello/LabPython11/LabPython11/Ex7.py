def Ex7(file):
    import re
    d={'invalidi': 0, 'domestici': 0, 'altri': 0}
    
    f=open(file, encoding='UTF-8')
    r=f.read()
    f.close()
    r=r.strip().split('\n')
    pattern=r'\d{1,3}\D\d{1,3}\D\d{1,3}\D\d{1,3}'
    for i in r:
        m=re.search(pattern,i,re.IGNORECASE)
        if m:
            if re.search(r'192.168.',i):
                d['domestici']=d['domestici']+1
            else:
                d['altri']=d['altri']+1
        else:
            d['invalidi']=d['invalidi']+1
    return d
    
###############################################################################

if __name__ == '__main__':
    from tester import tester_fun
    import re

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex7, ["ip1.txt"] , {'invalidi': 0, 'domestici': 0, 'altri': 5})
    counter_test_positivi += tester_fun(Ex7, ["ip2.txt"] , {'invalidi': 2, 'domestici': 1, 'altri': 2})
    counter_test_positivi += tester_fun(Ex7, ["ip3.txt"] , {'invalidi': 1, 'domestici': 1, 'altri': 3})
    counter_test_positivi += tester_fun(Ex7, ["ip4.txt"] , {'invalidi': 1, 'domestici': 1, 'altri': 3})
    counter_test_positivi += tester_fun(Ex7, ["ip5.txt"] , {'invalidi': 3, 'domestici': 0, 'altri': 2})
    
    print('La funzione',Ex7.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
