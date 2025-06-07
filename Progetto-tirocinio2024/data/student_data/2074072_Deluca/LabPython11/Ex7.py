def Ex7(file):
    f=open(file, encoding="UTF-8")
    l=[]
    for line in f:
        elem=line.strip()
        l.append(elem)
    d={'invalidi': 0, 'domestici': 0, 'altri': 0}
    pattern="([0-9]*)\.([0-9]*)\.([0-9]*)\.([0-9]*)"
    for elem in l:
        mn = re.finditer(pattern, elem)
        for m in mn:
            if int(m.group(1)) in range(256) \
            and int(m.group(2)) in range(256) \
            and int(m.group(3)) in range(256) \
            and int(m.group(4)) in range(256) \
            and len(m.group(1)) in range(1,4) \
            and len(m.group(2)) in range(1,4) \
            and len(m.group(3)) in range(1,4) \
            and len(m.group(4)) in range(1,4):
                if int(m.group(1))==192 and int(m.group(2))==168:
                    d["domestici"]+=1
                else:
                    d["altri"]+=1
            else:
                d["invalidi"]+=1
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
