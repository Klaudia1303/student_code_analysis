def Ex7(file):
    lip=open(file,encoding='UTF-8')
    pattern=r'([0-9]{4}|[0]?[01]?[0-9]{1,2}|2[1234][0-9]|255)\.([0-9]{4}|[0]?[01]?[0-9]{1,2}|2[1234][0-9]|255)\.([0-9]{4}|[0]?[01]?[0-9]{1,2}|2[1234][0-9]|255)\.([0-9]{4}|[0]?[01]?[0-9]{1,2}|2[1234][0-9]|255|[0-9]{4})'
    d={'domestici':0,'invalidi':0,'altri':0}
    for ip in lip:
        m=re.search(pattern,ip)
        print(ip)
        c=False
        for i in range(1,5):
            print(m.group(i))
            if len(str(m.group(i))) >3:
                d['invalidi']+=1
                print(d)
                c=True
        if c:
            continue
        if m:
            n1=int(m.group(1))
            n2=int(m.group(2))
            if n1==192 and n2==168:
                d['domestici']+=1
            else:
                d['altri']+=1
        else:
            d['invalidi']+=1
        print(d)
    return d
            
    
###############################################################################

if __name__ == '__main__':
    from tester import tester_fun
    import re

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex7, ["ip1.txt"] , {'invalidi': 0, 'domestici': 0,'altri': 5})
    counter_test_positivi += tester_fun(Ex7, ["ip2.txt"] , {'invalidi': 2, 'domestici': 1, 'altri': 2})
    counter_test_positivi += tester_fun(Ex7, ["ip3.txt"] , {'invalidi': 1, 'domestici': 1, 'altri': 3})
    counter_test_positivi += tester_fun(Ex7, ["ip4.txt"] , {'invalidi': 1, 'domestici': 1, 'altri': 3})
    counter_test_positivi += tester_fun(Ex7, ["ip5.txt"] , {'invalidi': 3, 'domestici': 0, 'altri': 2})
    
    print('La funzione',Ex7.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
