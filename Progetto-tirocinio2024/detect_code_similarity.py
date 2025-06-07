import os
import ast
import hashlib
import itertools
import pandas as pd
from tqdm import tqdm
import sys

def load_all_python_files(base_dir, lab_filter=None):
    """Carica tutti i file .py con opzione filtro sul nome del laboratorio."""
    file_contents = []
    for student_folder in os.listdir(base_dir):
        student_path = os.path.join(base_dir, student_folder)
        if not os.path.isdir(student_path):
            continue
        for root, _, files in os.walk(student_path):
            # Se specificato, ignora cartelle diverse dal Lab scelto
            if lab_filter and lab_filter not in root:
                continue
            for f in files:
                if not f.endswith(".py"):
                    continue
                if "tester" in f.lower():
                    continue
                path = os.path.join(root, f)
                try:
                        with open(path, "r", encoding="utf-8", errors="ignore") as file:
                            code = file.read()
                            file_contents.append({
                                "student": student_folder,
                                "file": f,
                                "path": path,
                                "code": code
                            })
                except Exception as e:
                        print(f"Errore nella lettura di {path}: {e}")
    return file_contents

def ast_structure(code):
    try:
        tree = ast.parse(code)
        return [type(node).__name__ for node in ast.walk(tree)]
    except:
        return []

def compare_codes(file_list, max_pairs=None):
    results = []
    combinations = list(itertools.combinations(file_list, 2))
    total = len(combinations)
    print(f"🔢 Numero totale di confronti possibili: {total}")
    count = 0

    for f1, f2 in tqdm(combinations, desc="Confronti esercizi con stesso nome"):
        
        if f1["file"] != f2["file"]:
            continue
        count += 1 
        if max_pairs and count > max_pairs:
            break
        
        hash1 = hashlib.md5(f1["code"].strip().encode()).hexdigest()
        hash2 = hashlib.md5(f2["code"].strip().encode()).hexdigest()
        identical = hash1 == hash2

        ast1 = ast_structure(f1["code"])
        ast2 = ast_structure(f2["code"])
        structure_similar = ast1 == ast2 if ast1 and ast2 else False

        if identical or structure_similar:
            results.append({
                "studente_1": f1["student"],
                "studente_2": f2["student"],
                "file": f1["file"],
                "identico_testuale": identical, 
                "simile_ast": structure_similar
            })

            file_output_dir = "reports/sospetti"
            os.makedirs(file_output_dir, exist_ok=True)
            output_name = f"diff_{f1['file'].replace('.py', '')}_{f1['student']}_vs_{f2['student']}.txt"
            output_path = os.path.join(file_output_dir, output_name)

            with open(output_path, "w", encoding="utf-8") as out: 
                out.write(f"=== {f1['student']} - {f1['file']} ===\n")
                out.write(f"{f1['code']}\n")
                out.write("=" * 60 + "\n")
                out.write(f"=== {f2['student']} - {f2['file']} ===\n")
                out.write(f"{f2['code']}\n")
    print (f"Confront effettuatu tra file con stesso nome: {count}")        
    return results

if __name__ == "__main__":
    base_dir = "data/student_data"
    os.makedirs("reports", exist_ok=True)

    # ↪️ Lettura filtro lab dalla riga di comando
    lab_filter = sys.argv[1] if len(sys.argv) > 1 else None
    label = f"_{lab_filter}" if lab_filter else ""
    output_csv = f"reports/code_similarity_filtered{label}.csv"

    print(f"📥 Caricamento file Python degli studenti{' dal lab ' + lab_filter if lab_filter else ''}...")
    files = load_all_python_files(base_dir, lab_filter)
    print(f"✅ Trovati {len(files)} file da confrontare.")

    print("🔍 Avvio analisi per esercizi con stesso nome...")
    results = compare_codes(files)

    if results:
        df = pd.DataFrame(results)
        df.to_csv(output_csv, index=False)
        print(f"✅ Sono stati rilevati {len(df)} casi sospetti.")
        print(f"📄 Report salvato in {output_csv}")
    else:
        print("✅ Nessun caso sospetto rilevato.")
