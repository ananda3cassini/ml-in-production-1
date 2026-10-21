from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

# le modèle est chargé une seule fois au démarrage du serveur
model = joblib.load("regression.joblib")


class House(BaseModel):
    size: float
    nb_rooms: int
    garden: int


@app.post("/predict")
def predict(house: House):
    y_pred = model.predict([[house.size, house.nb_rooms, house.garden]])
    return {"y_pred": y_pred[0]}
