from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model import predict

app = FastAPI()

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class NewsItem(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Fake News Detection API"}

@app.post("/predict/")
def predict_news(news_item: NewsItem):
    prediction = predict(news_item.text)
    return {"text": news_item.text, "result": prediction}