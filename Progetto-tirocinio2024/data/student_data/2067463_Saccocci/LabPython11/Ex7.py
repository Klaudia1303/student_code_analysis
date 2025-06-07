def Ex7(file):
    import re
    f=open(file,'r',encoding='UTF-8')
    d={}
    d['invalidi']=0
    d['domestici']=0
    d['altri']=0
    for riga in f:
        pattern=r'(\b\d?\d?\d\b)[.](\b\d?\d?\d\b)[.](\b\d?\d?\d\b)[.](\b\d?\d?\d\b)'
        i=re.search(pattern,riga)
        if i:
            primo=int(i.group(1))
            secondo=int(i.group(2))
            terzo=int(i.group(3))
            quarto=int(i.group(4))
            if 0<=primo<=255 and 0<=secondo<=255 and 0<=terzo<=255 and 0<=quarto<=255:
                if primo==192 and secondo==168:
                    d['domestici']+=1
                else:
                    d['altri']+=1
            else:
                d['invalidi']+=1
        else:
            d['invalidi']+=1
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
