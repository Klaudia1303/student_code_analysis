def Ex4(file):
    f = open(file,'r',encoding= 'UTF-8')
    intestazione = f.readline().strip().split(',')
   # print(intestazione)
    d = dict()

    for riga in f:
        r = riga.strip().split(',')
       # print(r)
        oggetto = r[0]
        proprietario = r[1]
        erede = r[2]

        if oggetto not in d:
            d[oggetto] = [[proprietario],[erede]]
            #print('if',d)

        #print((d[oggetto][1]),proprietario)

        elif (oggetto in d) and (d[oggetto][1] == [proprietario]) :
            d[oggetto][1] = [erede]
            #print('elif',d)
    #print(d)
    risultato = list()

    for k in d:
        x = d[k][0]
        y = d[k][1]
        #print(x,y)
        z = x + y
        d[k] = z
    #print('finale',d)

    return d
    
        
        




    
            

    
    
    
    
  
    
            

       


      
        

    

    

     
    
    











    
    
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
