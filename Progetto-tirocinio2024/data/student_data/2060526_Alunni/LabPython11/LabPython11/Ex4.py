def Ex4(file):
    d={}
    c=open(file, encoding= 'UTF-8')
    C=c.readlines()
    h=[]
    for i in C[1:]:
        S=i.strip().split(',')
        h.append(S)
    for i in h:
            
        if i[0] not in d:
            d[i[0]]=[]
            d[i[0]].append(i[1])
            d[i[0]].append(i[2])
            
        if i[0] in d and d[i[0]][1]==i[1]:
            
            
            d[i[0]].remove(d[i[0]][1])
            d[i[0]].append(i[2])
        
            

            
                
        
            
            
      
            
        
                
        
    c.close()  
    return d
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex4, ["eredita1.csv"] , {'Anello_di_smeraldi': ['Maria', 'Giorgia'], 'Anello': ['Silvia', 'Paolo']})
    counter_test_positivi += tester_fun(Ex4, ["eredita2.csv"] , {'Anello_di_smeraldi': ['Marco', 'Giorgio'], 'Anello': ['Silvia', 'Sergio']})
    counter_test_positivi += tester_fun(Ex4, ["eredita3.csv"] , {'Anello_di_smeraldi': ['Marco', 'Giorgio'], 'Anello': ['Silvia', 'Sergio'], 'Vaso': ['Anna', 'Sergio']})
    counter_test_positivi += tester_fun(Ex4, ["eredita4.csv"] , {'Anello_di_smeraldi': ['Marco', 'Giorgio'], 'Anello': ['Silvia', 'Giorgio'], 'Vaso': ['Anna', 'Anna']})
    counter_test_positivi += tester_fun(Ex4, ["eredita5.csv"] , {'Anello_di_smeraldi': ['Marco', 'Giorgio'], 'Anello': ['Silvia', 'Sergio'], 'Vaso': ['Sergio', 'Anna']})

    print('La funzione',Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
