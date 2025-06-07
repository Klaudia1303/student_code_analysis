def Ex7(file):
    fin=open(file,encoding="UTF-8")
    d={"domestici":0,"invalidi":0,"altri":0}
    for riga in fin:
        ri=riga.strip().split(".")
        if (int(ri[0])<=255 and int(len(ri[0])<=3)) and (int(ri[1])<=255 and int(len(ri[1])<=3)) and (int(ri[2])<=255 and int(len(ri[2]))<=3) and (int(ri[3])<=255 and int(len(ri[3]))<=3):
            if int(ri[0])==192 and int(ri[1])==168:
                d["domestici"]+=1
            else:
                d["altri"]+=1
        else:
            d["invalidi"]+=1
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
