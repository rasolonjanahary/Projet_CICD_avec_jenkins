from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from pydantic import BaseModel
import pandas as pd
import joblib
app = FastAPI()

class WiForm(BaseModel):
    fixed_acidity       :float
    volatile_acidity    :float
    citric_acid         :float
    residual_sugar      :float
    chlorides           :float
    free_sulfur_dioxide :float
    total_sulfur_dioxide:float
    density             :float
    pH                  :float
    sulphates           :float
    alcohol             :float 
    type                :int

model = joblib.load("models/model_dc.pkl")
sc = joblib.load("models/scaler1.pkl")

# model = joblib.load("../models/model_dc.pkl")
# sc = joblib.load("../models/scaler1.pkl")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api")
def home():
    return {"message": "API OK"}

@app.post("/predict")
def predict(data: WiForm):
    input_dict = {
            "fixed_acidity": data.fixed_acidity,
            "volatile_acidity": data.volatile_acidity,
            "citric_acid": data.citric_acid,
            "residual_sugar": data.residual_sugar,
            "chlorides": data.chlorides,
            "free_sulfur_dioxide": data.free_sulfur_dioxide,
            "total_sulfur_dioxide": data.total_sulfur_dioxide,
            "density": data.density,
            "pH": data.pH,
            "sulphates": data.sulphates,
            "alcohol": data.alcohol,
            "type": data.type,
        }

    df = pd.DataFrame([input_dict])
    xc = sc.transform(df)
    pred = model.predict(xc)
    return {"prediction": int(pred[0])}