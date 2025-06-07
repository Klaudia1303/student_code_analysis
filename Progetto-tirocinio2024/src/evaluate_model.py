# Evaluation and metrics
import torch.nn as nn 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
from train_model import CodeClassifier

def evaluate_model (cv_path, model_path):
    #Carica dati 
    df = pd.read_csv(csv_path)
    X = df.drop(columns= ["student"]).values
    y = LabelEncoder().fit_transform(df["student"])
    label_names = sorted(df["student"].unique())

    #Normalizza 
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_tensor = torch.tensor(X_scaled, dtype = torch.float32)

    #Carica modello 
    model = CodeClassifier(input_dim=X.shape[1], hidden_dim=64, output_dim=len(set(y)))
    model.load_state_dict(torch.load(model_path))
    model.eval()

    #Predizione 
    with torch.no.grad():
        predictions = model (X_tensor).argmax(dim=1).numpy()

    #Report
    print("\nREPORT DI CLASSIFICAZIONE:\n")
    print(classification_report(y, predictions, target_names=label_names))

    #Matrice di confusione
    cm = confusion_matrix(y, predictions)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, ftm='d',xticklabels=label_names, yticklabels=label_names, cmap="Blues")
    plt.ylabel("Predetto")
    plt.ylabel("Reale")
    plt.title("Matrice di confusione")
    plt.tight_layout()
    plt.savefig("reports/confusion_matrix.png")
    print("Matrice di confusione salvata in reports/confusion_matrix.png")

if __name__ == "__main__":
    evaluate_model("dataset/extracted_features.csv", "models/code_classifier.pth")