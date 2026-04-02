import pandas as pd
import joblib

model = joblib.load("../models/model_dc.pkl")
sc = joblib.load("../models/scaler1.pkl")

dic = {
  "fixed_acidity": 7.3,
  "volatile_acidity": 0.6,
  "citric_acid": 0,
  "residual_sugar": 1.8,
  "chlorides": 0.075,
  "free_sulfur_dioxide": 10,
  "total_sulfur_dioxide": 33,
  "density": 0.98,
  "pH": 3.50,
  "sulphates": 0.55,
  "alcohol": 9.3,
  "type": 1
}


df = pd.DataFrame([dic])
xc = sc.transform(df)
pred = model.predict(xc)

print(pred)