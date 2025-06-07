def Ex7(file):
    f=open(file,encoding="UTF-8")
    l=[]
    for riga in f:
        l.append(riga.strip().split("."))
    d={}
    d['invalidi']=0
    d['domestici']=0
    d['altri']=0
    for i in range(len(l)):
        if len(l[i][0])>3 or len(l[i][1])>3 or len(l[i][2])>3 or len(l[i][3])>3:
            d['invalidi']+=1
        elif int(l[i][0])>255 or int(l[i][1])>255 or int(l[i][2])>255 or int(l[i][3])>255:
            d['invalidi']+=1
        elif int(l[i][0])==192 and int(l[i][1])==168:
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
