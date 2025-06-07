def Ex7(file):
    fopen=open(file,'r',encoding='UTF-8')
    d={}
    d['invalidi']=0
    d['domestici']=0
    d['altri']=0
    for riga in fopen:
        riga=riga.strip().split('.')
        if (int(riga[0])<0 or int(riga[0])>255) or (int(riga[1])<0 or int(riga[1])>255) or (int(riga[2])<0 or int(riga[2])>255) or (int(riga[3])<0 or int(riga[3])>255) or len(riga)>4 or len(riga[0])>3 or len(riga[1])>3 or len(riga[2])>3 or len(riga[3])>3:
            d['invalidi']=int(d['invalidi'])+1
        elif int(riga[0])==192 and int(riga[1])==168:
            if 0<=int(riga[2])<=255 and 0<=int(riga[3])<=255:
                print(riga)
                d['domestici']=int(d['domestici'])+1
            else:
                d['invalidi']=int(d['invalidi'])+1
        elif int(riga[0])!=192 and int(riga[1])!=168:
            if 0<=int(riga[0])<=255 and 0<=int(riga[1])<=255 and 0<=int(riga[2])<=255 and 0<=int(riga[3])<=255:
                d['altri']=int(d['altri'])+1
        elif int(riga[0])!=192 and int(riga[1])==168 or int(riga[0])==192 and int(riga[1])!=168:
            d['altri']=int(d['altri'])+1
        
        
        
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
