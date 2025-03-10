from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define input format
class TextInput(BaseModel):
    text: str

@app.post("/text-input/")
async def process_text(input_data: TextInput):
    user_text = input_data.text

    # Simple NLP: Detect Loan-Related Keywords
    loan_keywords = ["loan", "credit", "borrow", "interest"]
    if any(keyword in user_text.lower() for keyword in loan_keywords):
        response = {"message": "Looks like you're asking about a loan!", "user_text": user_text}
    else:
        response = {"message": "We received your text!", "user_text": user_text}
    
    return response
