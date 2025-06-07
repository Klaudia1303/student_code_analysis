def Ex7(file):
    d={'invalidi':0, 'domestici':0, 'altri':0}
    f=open(file, encoding='UTF-8')
    l=f.readlines()
    f.close()
    for i in range(len(l)):
        cond=True
        r=l[i].strip().split('.')
        for j in range(len(r)):
            if(len(r[j])>3 or int(r[j])>255):
                cond=False
                break
        if(not cond):
            d['invalidi']+=1
            continue
        if(int(r[0])!=192 or int(r[1])!=168):
            d['altri']+=1 
        else:
            d['domestici']+=1 
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
