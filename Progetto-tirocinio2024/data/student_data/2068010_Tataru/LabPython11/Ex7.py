def Ex7(file):
    import re
    d={'invalidi':0, 'domestici':0, 'altri':0}
    f = open(file,encoding="UTF-8")
    fr=f.read().split()
    for el in fr:
        c=True
        a=re.search(r'\b\d?\d?\d\.\d?\d?\d\.\d?\d?\d\.\d?\d?\d\b',el)
        dm=re.search(r'\b192\.168\.\d?\d?\d\.\d?\d?\d\b',el)
        if dm:
            for i in el.split('.'):
                if int(i)>255:
                    c=False
                    break
            if c==True:
                d['domestici']+=1
        elif a:
            for i in el.split('.'):
                if int(i)>255:
                    c=False
                    break
            if c==True:
                d['altri']+=1
        else:
            d['invalidi']+=1
        a=dm=None
        if c==False:
            d['invalidi']+=1
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
