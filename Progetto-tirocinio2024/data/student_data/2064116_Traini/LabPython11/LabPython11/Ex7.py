#Ex7(file): un indirizzo IP è un’etichetta numerica che identifica univocamente un dispositivo all’interno 
#di una rete informatica. Esso è costituito da una sequenza di 4 numeri compresi tra 0 e 255, formati da 
#una, due o tre cifre e separati da un punto, (es. 192.168.0.1). Tra tutti i possibili indirizzi IP, vi è un 
#intervallo dedicato alle reti domestiche, i quali hanno formato 192.168.X.Y, dove X ed Y sono due numeri 
#compresi tra 0 e 255. Scrivere la funzione Python che preso in ingresso il nome di un file di testo avente 
#il seguente formato
#Indirizzo_IP
#Indirizzo_IP
#[…]
#Indirizzo_IP
#e restituisca un dizionario contenente le seguenti chiavi: ‘invalidi’, ‘domestici’ ed ‘altri’, e come valori 
#associati il numero di indirizzi letti dal file che sono rispettivamente non validi, domestici oppure validi 
#non domestici
import re
def Ex7(file):
    risultato={'invalidi':0,'domestici':0,'altri':0}
    pattern=r'[0-9]{3},[0-9]{3},[0-9]{3},[0-9]{3}'
    fin=open(file,encoding='utf-8')
    verifica=False
    for riga in fin:
        casa=riga.strip().split('.')
        for elem in casa:
            if int(elem)>255 or len(str(elem))>3:
                verifica=True
        if verifica:
            risultato['invalidi']+=1
        elif int(casa[0])==192 and int(casa[1])==168:
            risultato['domestici']+=1
        else:
            risultato['altri']+=1
        verifica=False
    return risultato
            
        
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
