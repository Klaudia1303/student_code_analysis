def Ex7(file):
    f=open(file,'r',encoding='UTF-8')
    campi=['invalidi','domestici','altri']
    d={}
    for campo in campi:
        d[campo]=0
    for line in f:
        line=line.strip().split('.')
        valido=True
        domestico=False
        if len(line)!=4:
            valido=False
        if line[0]=='192' and line[1]=='168':
            domestico=True
        for n in line:
            if int(n)>255 or len(n)>3:
                valido=False
        if valido and domestico:
            d['domestici']+=1
        if not valido:
            d['invalidi']+=1
        if valido and not domestico:
            d['altri']+=1
    f.close()
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
