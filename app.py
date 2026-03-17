from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all (fine for your project)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# load model (pipeline)
model = pickle.load(open("model.pkl", "rb"))

# median fare mapping
fare_map = {
    1: 84.19,
    2: 20.66,
    3: 13.67
}

@app.get("/")
def home():
    return {"message": "Titanic Survival API"}

@app.post("/predict")
def predict(data: dict):
    # handle missing Fare
    if "Fare" not in data or data["Fare"] is None:
        data["Fare"] = fare_map[data["Pclass"]]

    # convert to DataFrame
    features = pd.DataFrame([data])

    prediction = model.predict(features)

    return {"survived": int(prediction[0])}