from fastapi import FastAPI
from typing import List, Dict
import json

app = FastAPI()

# Load questions from questions.json
with open("questions.json", "r") as file:
    questions = json.load(file)

@app.get("/questions", response_model=List[Dict[str, str]])
async def get_questions():
    return questions

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)