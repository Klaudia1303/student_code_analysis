def Ex7(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""    
    with open(file,"r",encoding="UTF-8") as f:
        d={}
        cont=0
        chiavi=['invalidi','domestici','altri']
        for x in chiavi:
            d[x]=0
        for righe in f:
            cont+=1
            riga=righe.strip().split(".")
            print(riga)
            c=False
            for i in riga:
                if int(i) not in range(0,256) or len(i)>3:
                    d['invalidi']+=1
                    print("invalido: ",i," in ",riga)
                    c=True
                    break
            
            if riga[0]=='192' and riga[1]=='168' and int(riga[2]) in range(0,256) and int(riga[3]) in range(0,256) and not c:
                d['domestici']+=1
               
        d['altri']=(cont-d['invalidi']-d['domestici'])
                
    return d


            #pattern_altri=r'\b[0-9]{,3}'+'.'+r'[0-9]{,3}'+'.'+r'[0-9]{,3}'+'.'+r'[0-9]{,3}$'
            #pattern_domestici=





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
