def A_Ex6(filename):
    l=[]
    l2=[]
    l4=[]
    l5=[]
    j=0
    n=0
    p=0
    sum=0
    sum2=0
    sum3=0
    sum4=0
    f=open(filename, 'r', encoding='UTF-8')
    s=f.readline()
    l=s.strip().split(',')

    for riga in f:
        l2.append(riga.strip().split(','))
    
    for ele in l2:
        p+=1
        
    for m in ele:
            j+=1
    
    for ele in l2:
        if j<=4:
            sum+=int(ele[1])
            sum2+=int(ele[2])
            sum3+=int(ele[3])
        elif j==5:
            sum+=int(ele[1])
            sum2+=int(ele[2])
            sum3+=int(ele[3])
            sum4+=int(ele[4])

    l4.append(sum)
    l4.append(sum2)
    l4.append(sum3)

    if(j==5):
        l4.append(sum4)

    n=max(l4)
    pos=l4.index(n)

    l5=s.strip().split(',')

    ris=int(l5[pos+1])

    return ris
      
 
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex6, ['Vendite1.csv'] , 2010)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite2.csv'] , 2013)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite3.csv'] , 2013)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite4.csv'] , 2020)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite5.csv'] , 2022)

    print('La funzione',A_Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
