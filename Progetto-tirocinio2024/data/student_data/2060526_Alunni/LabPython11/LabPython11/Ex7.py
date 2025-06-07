def Ex7(file):
    d={}
    c=open(file, encoding= 'UTF-8')
    d={'invalidi':0,'domestici':0,'altri':0}
    p1=r'\b(\d?\d?\d)\.(\d?\d?\d)\.(\d?\d?\d)\.(\d?\d?\d)\b'
    p2=r'\b192\.168\.(\d?\d?\d)\.(\d?\d?\d)\b'
    for i in c:
        m1= re.search(p1,i)
        m2= re.search(p2,i)
        if m2:
            if int(m2.group(1))<=255 and int(m2.group(2))<=255:
                d['domestici']+=1
            else:
                d['invalidi']+=1
        elif m1:
            if int(m1.group(1))<=255 and int(m1.group(2))<=255 and int(m1.group(3))<=255 and int(m1.group(4))<=255:
                d['altri']+=1
            else:
                d['invalidi']+=1
        else:
            d['invalidi']+=1
    c.close()
    return d


    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""    
    
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
