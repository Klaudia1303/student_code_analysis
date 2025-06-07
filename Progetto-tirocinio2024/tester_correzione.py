from threading import Thread 
import traceback
import ctypes
import sys
import os

def tester_fun_correzione(function, input_data, output_data,file_path):

    """

    :param function: funzione da testare
    :param input_data: input in formato tupla
    :param output_data: output
    :param file_path: file dove appendere l'esito del test
    :return:
        -1 invocazione errata
        0 problema in esecuzione
        1 test superato
    """

    with open(file_path,'a', encoding="utf-8") as outputfile:

        # secondi disponibili per l'esecuzione della funzione
        timeout = 5

        # BASIC CHECKS su input ed output del tester
        if not isinstance(input_data, list):
            print("ERRORE: l'input data deve essere fornito all'interno di una lista")
            return -1

        if len(input_data)==0 or output_data == None:
            print("ERRORE: input o output non regolare")
            return -1

        outputfile.write('Test'+' '+function.__name__+' '+'\n\n')
        outputfile.write('Input:'+' '+str(input_data)[1:-1]+' '+'\n\n')

        outputfile.write('Output atteso:\n')
        outputfile.write("-"* 34+'\n')
        outputfile.write(str([output_data])[1:-1]+'\n')
        outputfile.write("-"* 34+'\n\n')

        result_container = []

        # comandi sospensione print all'interno delle funzioni
        stdout = sys.stdout
        null = open(os.devnull, 'w')
        sys.stdout = null

        # la funzione viene eseguita all'interno di un thread, in modo da gestire i loop
        t = Thread(target=helper_tester_function, args=(function, input_data, result_container))
        t.daemon = True
        t.start()
        t.join(timeout)
        # se il thread è ancora alive allo scadere del timeout, probabilmente vi è un loop
        if (sys.version_info[:2] >= (3,8) and t.is_alive()) or (sys.version_info[:2] < (3,8) and t.isAlive()):
            terminate_thread(t)

            sys.stdout = stdout    # decommentare nel caso si disattivino le print
            outputfile.write('Il codice sta impiegando più del previsto a fornire il suo output, potrebbe essere presente un ciclo infinito\n')
            outputfile.write('Risultato Test: NEGATIVO'+'\n\n'+'*'*30+'\n')
            return 0

        # il risultato o l'eccezione generata vengono inseriti in result_container
        else:
            sys.stdout = stdout    # decommentare nel caso si disattivino le print
            # nessun valore di ritorno
            if len(result_container) == 0 or result_container[0] == None:
                outputfile.write('Risultato Test: NEGATIVO, nessun output'+'\n\n'+'*'*30+'\n')
                return 0

            # in caso di eccezione
            elif isinstance(result_container[0],Exception):
                outputfile.write('Il codice ha lanciato una eccezione durante il test\n\n')
                outputfile.write(result_container[1]+'\n')
                outputfile.write('Risultato Test: NEGATIVO'+'\n\n'+'*'*30+'\n')
                return 0
            else:
                # in caso di valore di ritorno fornito
                outputfile.write('Output ottenuto:\n')
                outputfile.write("-"* 34+'\n')
                outputfile.write(str([result_container[0]])[1:-1]+'\n') 
                outputfile.write("-"* 34+'\n\n')
                if output_data != result_container[0]:
                    outputfile.write('Risultato Test: NEGATIVO'+'\n\n'+'*'*30+'\n')
                    return 0
                else:
                    outputfile.write('Risultato Test: POSITIVO'+'\n\n'+'*'*30+'\n')
                    return 1



def helper_tester_function(function, input_data, return_value_container):
    """

    Funzione interna, definita per gestire le eccezioni
    """
    try:
        returned_value = function(*input_data)
        return_value_container.append(returned_value)
    except Exception as e:
        return_value_container.append(e)
        return_value_container.append(traceback.format_exc())

def terminate_thread(t):
    """

    Funzione interna, termina un thread
    """
    exec = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(t.ident), exec)
    if res == 0:
        print("thread not found!")
    elif res > 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(t.ident), None)