# PyTorch training script

import torch
import torch.nn as nn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from torch.utils.data import DataLoader, TensorDataset

class CodeClassifier (nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(CodeClassifier, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, output_dim)
        )
    def forward(self, x):
        return self.net(x)
def train_model(csv_path, model_path):
    #Caricamento dati 
    df = pd.read_csv(csv_path)
    X = df.drop(columns=["student"]).values
    y = LabelEncoder().fit_transform(df["student"])

    #Normalizzazione
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    #Split training/test
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    #Tensors
    X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
    y_train_tensor = torch.tensor(y_train, dtype=torch.long)

    dataset = TensorDataset(X_train_tensor, y_train_tensor)
    Dataloader = DataLoader(dataset, batch_size = 8, shuffle= True)

    model = CodeClassifier(input_dim=X.shape[1], hidden_dim=64, output_dim=len(set(y)))
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    #Training Loop
    for epoch in range(50):
        total_loss = 0
        for xb, yb in dataloader: 
            preds = model(xb)
            loss = criterion(preds, yb)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        if epoch % 10 ==0:
            print(f"Epoch {epoch}: Loss = {total_loss: .4f}")

    #Salva il modello 
    torch.save(model.state_dict(), model_path)
    print(f"Modello salvato in {model_path}")

if __name__ == "__main__":
    train_model("dataset/extracted_features.csv", "models/code_classifier.pth")



