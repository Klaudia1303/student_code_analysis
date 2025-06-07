def Ex7(file):
    f=open(file)
    s=f.read()
    d={'invalidi':0,'domestici':0,'altri':0}
    pattern=r'\b([0-9]*)\.([0-9]*)\.([0-9]*)\.([0-9]*)\b'
    i=re.finditer(pattern,s)
    for m in i:
        n1=int(m.group(1))
        n2=int(m.group(2))
        n3=int(m.group(3))
        n4=int(m.group(4))
        if n1>255 or n2>255 or n3>255 or n4>255 or len(m.group(1))>3 or len(m.group(2))>3 or len(m.group(3))>3 or len(m.group(4))>3:
            d['invalidi']+=1
        elif n1==192 and n2==168 and n3<255 and n4<255 and len(m.group(1))<=3 and len(m.group(2))<=3:
            d['domestici']+=1
        else:
            d['altri']+=1
            
    f.close()
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
