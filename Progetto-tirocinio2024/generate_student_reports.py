import pandas as pd
import os

def generate_reports(csv_path, output_dir):
    df = pd.read_csv(csv_path)
    os.makedirs(output_dir, exist_ok=True)
    grouped = df.groupby("studente")

    for student, group in grouped:
        report_path = os.path.join(output_dir, f"report_{student}.txt")
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(f"RAPPORTO TEST PER STUDENTE: {student}\n")
            f.write("="*40 + "\n\n")
            for _, row in group.iterrows():
                f.write(f"Lab: {row['lab']}, File: {row['file']}, Funzione: {row['funzione']}\n")
                f.write(f"Input: {row['input']}\n")
                f.write(f"Output atteso: {row['output_atteso']}\n")
                f.write(f"Esito: {'✔ SUPERATO' if row['esito'] == 1 else '✘ FALLITO'}\n")
                f.write("-"*30 + "\n\n")
            f.write(f"Totale esercizi testati: {len(group)}\n")
            f.write(f"Superati: {sum(group['esito'] == 1)}\n")
            f.write(f"Falliti: {sum(group['esito'] == 0)}\n")
            f.write(f"Errori: {sum(group['esito'] == -1)}\n")

    print(f"✅ Report individuali generati in {output_dir}")

if __name__ == "__main__":
    generate_reports("reports/risultati_lab07.csv", "reports/studenti/")
