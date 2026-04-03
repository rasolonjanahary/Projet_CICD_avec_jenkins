import mlflow
import pandas as pd
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer

mlflow.set_experiment("wine")

df = pd.read_csv("data/wine_equilibre.csv")
#df = pd.read_csv("../data/wine_equilibre.csv")


df = df.rename(columns={
    "fixed acidity":"fixed_acidity",
    "volatile acidity":"volatile_acidity",
    "citric acid":"citric_acid",
    "residual sugar":"residual_sugar",
    "free sulfur dioxide":"free_sulfur_dioxide",
    "total sulfur dioxide":"total_sulfur_dioxide"
})

X = df.drop("quality", axis=1)
X["type"] = X["type"].apply(lambda x: 1 if x=="white" else 0)
df["quality"] = df["quality"].apply(lambda x: 1 if x=="Legit" else 0)
y = df["quality"]


num_cols = [col for col in X.columns if col != "type"]

preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), num_cols),
        ("cat", "passthrough", ["type"])
    ]
)

X_scaled = preprocessor.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y)

model = RandomForestClassifier()

with mlflow.start_run():
    model.fit(X_train, y_train)
    acc = model.score(X_test, y_test)

    mlflow.log_metric("accuracy", acc)
    mlflow.sklearn.log_model(model, "model")
    mlflow.sklearn.log_model(preprocessor, "preprocessor")

    print("Accuracy:", acc)