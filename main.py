from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Email model
class Email(BaseModel):
    text: str

# Spam words database
spam_words = [
    "win",
    "free",
    "money",
    "lottery",
    "offer",
    "prize",
    "urgent",
    "claim",
    "winner",
    "cashback",
    "credit card",
    "payment",
    "login"
]

# API route
@app.post("/predict")
def predict(email: Email):

    text = email.text.lower()

    detected = []

    # Check spam words
    for word in spam_words:

        if word in text:

            detected.append(word)

    # Spam score
    spam_score = len(detected) * 15

    if spam_score > 100:

        spam_score = 100

    # Result
    if len(detected) > 0:

        result = "SPAM"

    else:

        result = "SAFE"

    return {
        "result": result,
        "score": spam_score,
        "detected_words": detected
    }