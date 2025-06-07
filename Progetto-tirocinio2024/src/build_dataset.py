# Dataset builder from student Python files
import os
import pandas as pd
from src import extract_features_from_code, check_code_errors # type: ignore

def build_dataset_from_folder(folder_path, output_csv):
    rows=[]

    for student_folder in os.listdir(folder_path):
        student_path = os.path.join(folder_path, student_folder)
        if not os.path.isdir(student_path):
            continue

        for filename in os.lisdir(student_path):
            if filename.endswith(".py"):
                file_path = os.path.join(student_path, filename)
                with open(file_path, "r", encoding= "utf-8", errors="ignore") as f:
                    code = f.read()
                    try: 
                        features = extract_features_from_code(code)
                        syntax_err, runtime_err, err_type = check_code_errors(code)
                        features["syntax_error"] = syntax_err
                        features["runtime_error"] = runtime_err
                        features["error_tyoe"] = err_type
                        features["student"] = student_folder
                        rows.append(features)
                    except Exception as e: 
                        print ("Errore nel parsing di {file_path}: {e}")
    df = pd.DataFrame(rows)
    if not df.empty:
        df["error_code"] = pd.factorize(df["error_type"])[0]
        df.drop(columns= ["error_type"], inplace = True)
        df.to_csv(output_csv, index=False)
        print(f"Dataset salvato in {output_csv}")
    else: 
        print("Nessun dato trovato. Dataset non generato.")
if __name__ == "__main__":
    build_dataset_from_folder("data/student_data", "dataset/extracted_features.csv")