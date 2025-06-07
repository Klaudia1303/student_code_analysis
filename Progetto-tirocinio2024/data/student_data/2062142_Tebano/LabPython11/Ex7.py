def Ex7(file):
    d={'invalidi':0,'domestici':0,'altri':0}
    L=[]
    e=0
    fin=open(file)
    for riga in fin:
        riga=riga.strip()
        L.append(riga)
    print(L)
    for indirizzo in L:
        e=0
        indirizzo=indirizzo.split('.')
        for valore in indirizzo:
            if int(valore)>255 or len(valore)>3:
                d['invalidi']+=1
                e=1
                break
        if e==0:
             if indirizzo[0:2]==['192','168']:
                   d['domestici']+=1
             else:
                   d['altri']+=1
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
