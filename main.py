from fastapi import FastAPI
from pydantic import BaseModel
from model import predict  # Change to absolute import

app = FastAPI()

class NewsItem(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Fake News Detection API"}

@app.post("/predict/")
def predict_news(news_item: NewsItem):
    prediction = predict(news_item.text)
    return {"prediction": prediction}
