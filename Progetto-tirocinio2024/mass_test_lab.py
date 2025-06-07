import os
import shutil
import importlib.util
import pandas as pd
from tester_correzione import tester_fun_correzione

def import_function_from_file(file_path, function_name):
    spec = importlib.util.spec_from_file_location("modulo_studente", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, function_name)

def test_all_students_for_lab(lab_folder_name, function_name, input_data, expected_output, output_csv):
    results = []
    student_base = "data/student_data"
    temp_dir = "temp_test_lab"
    os.makedirs(temp_dir, exist_ok=True)

    for student_folder in os.listdir(student_base):
        student_path = os.path.join(student_base, student_folder, lab_folder_name)
        if not os.path.isdir(student_path):
            continue

        for filename in os.listdir(student_path):
            if filename.endswith(".py"):
                full_path = os.path.join(student_path, filename)
                temp_file = os.path.join(temp_dir, "studente.py")
                shutil.copy(full_path, temp_file)

                try:
                    function = import_function_from_file(temp_file, function_name)
                    output_file = os.path.join(temp_dir, f"{student_folder}_output.txt")
                    esito = tester_fun_correzione(function, input_data, expected_output, output_file)

                    results.append({
                        "studente": student_folder,
                        "file": filename,
                        "lab": lab_folder_name,
                        "funzione": function_name,
                        "input": str(input_data),
                        "output_atteso": expected_output,
                        "esito": esito
                    })
                except Exception as e:
                    results.append({
                        "studente": student_folder,
                        "file": filename,
                        "lab": lab_folder_name,
                        "funzione": function_name,
                        "input": str(input_data),
                        "output_atteso": expected_output,
                        "esito": -1,
                        "errore": str(e)
                    })

    df = pd.DataFrame(results)
    df.to_csv(output_csv, index=False)
    print(f"✅ Test completato. Risultati salvati in {output_csv}")

if __name__ == "__main__":
    test_all_students_for_lab(
        lab_folder_name="Lab07",
        function_name="somma",
        input_data=[3, 5],
        expected_output=8,
        output_csv="reports/risultati_lab07.csv"
    )
