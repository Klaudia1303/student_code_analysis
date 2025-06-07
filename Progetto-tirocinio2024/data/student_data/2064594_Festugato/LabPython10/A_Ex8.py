def A_Ex8(file):
    f = open(file,'r',encoding = 'UTF-8')
    d = dict()

    intestazione = f.readline().strip().split(',')

    for riga in f :
        riga = riga.strip().split(',')

        n1 = riga[0]
        n2 = riga[1]
        rel = riga[2]


        d[n1] = d.get(n1,[])
        d[n2] = d.get(n2,[])

        
        if rel == 'amici':
            

            if n2 not in d[n1]:
                d[n1].append(n2) #aggiungi agli amici di n1 anche n2
                #print('d',type(d[n1]),d[n1])

            if n1 not in d[n2]:
                d[n2].append(n1) #aggiungi agli amici di n2 anche n1
            #print('amici',n1,d[n1],n2,d[n2])
            

        elif rel == 'nemici':
            if n2 in d[n1]:
                d[n1].remove(n2) #togli dagli amici di n1 anche n2

            if n1 in d[n2]:
                d[n2].remove(n1) #togli dagli amici di n2 anche n1
            #print('nemici',n1,d[n1],n2,d[n2])

        d[n1].sort()
        d[n2].sort()


    return d
 
            

            
            
            
            
            

        
        

        

    




































   
    
    
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex8, ["amici1.csv"] , {'Paolo': ['Marco'], 'Marco': ['Paolo'], 'Anna': ['Maria', 'Paola'], 'Maria': ['Anna'], 'Paola': ['Anna'], 'Giorgio': []})
    counter_test_positivi += tester_fun(A_Ex8, ["amici2.csv"] , {'Paolo': ['Marco'], 'Marco': ['Paolo'], 'Anna': ['Maria'], 'Maria': ['Anna'], 'Paola': [], 'Giorgio': []})
    counter_test_positivi += tester_fun(A_Ex8, ["amici3.csv"] , {'Paolo': ['Marco'], 'Marco': ['Paolo'], 'Anna': ['Maria', 'Paola'], 'Maria': ['Anna'], 'Paola': ['Anna'], 'Giorgio': []})
    counter_test_positivi += tester_fun(A_Ex8, ["amici4.csv"] , {'Marco': ['Giorgio', 'Paolo'], 'Giorgio': ['Marco'], 'Paolo': ['Marco'], 'Anna': ['Maria', 'Paola'], 'Maria': ['Anna'], 'Paola': ['Anna']})
    counter_test_positivi += tester_fun(A_Ex8, ["amici5.csv"] , {'Marco': [], 'Giorgio': [], 'Paola': [], 'Anna': []})

    print('La funzione',A_Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
