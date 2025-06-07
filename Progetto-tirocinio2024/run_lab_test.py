import shutil
import importlib.util
import os
from tester_correzione import tester_fun_correzione

def run_test(student_file, function_name, input_data, expected_output):
    temp_dir = "temp_test_lab"
    os.makedirs(temp_dir, exist_ok=True)
    target_file = os.path.join(temp_dir, "studente.py")

    shutil.copy(student_file, target_file)
    spec = importlib.util.spec_from_file_location("studente", target_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    function_to_test = getattr(module, function_name)
    output_file = os.path.join(temp_dir, "risultati.txt")

    risultato = tester_fun_correzione(function_to_test, input_data, expected_output, output_file)

    print("✔ Test completato.")
    print("📄 Risultato:", "PASSATO" if risultato == 1 else "FALLITO")
    print("📁 Output scritto in:", output_file)

if __name__ == "__main__":
    run_test(
        "data/student_data/1384133_Fichera/Lab07/esercizio7.py",
        "somma",
        [3, 5],
        8
    )
