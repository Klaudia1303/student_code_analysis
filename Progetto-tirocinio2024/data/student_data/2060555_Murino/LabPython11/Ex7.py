def Ex7(file):
    f=open(file)
    d={}
    d['invalidi']=0
    d['domestici']=0
    d['altri']=0
    for riga in f:
        riga=riga.strip().split('.')
        if len(riga)==4 and riga[0]=='192' and riga[1]=='168' and int(riga[2])<=255 and int(riga[3])<=255 and len(riga[2])<=3 and len(riga[3])<=3:
            d['domestici']+=1
        elif len(riga)!=4 or int(riga[0])>255 or int(riga[1])>255 or int(riga[2])>255 or int(riga[3])>255 or len(riga[0])>3 or len(riga[1])>3 or len(riga[2])>3 or len(riga[3])>3:
            d['invalidi']+=1
        elif len(riga)==4 and int(riga[0])<=255 and int(riga[1])<=255 and int(riga[2])<=255 and int(riga[3])<=255 and riga[0]!='192' or riga[1]!='168':
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
