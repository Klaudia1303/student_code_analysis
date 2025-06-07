def Ex7(file):
    f=open(file,'r',encoding='UTF-8')
    diz={'invalidi':0,'domestici':0,'altri':0}
    import re
    patDomest=r'\b192\.168\.\d\d?\d?\.\d\d?\d?\b'
    for riga in f:
        list=riga.strip().split('.')
        valoreProva=0
        for num in list:
            if 0<=int(num)<=255 and 1<=len(num)<=3:
                continue
            else:
                valoreProva=1
        if valoreProva==1:
            diz['invalidi']+=1
        elif re.match(patDomest,riga):
            diz['domestici']+=1
        else:
            diz['altri']+=1
    f.close()
    return diz
    
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
