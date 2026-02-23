from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PromptRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "IntelliPrompt Backend Running 🚀"}

@app.post("/generate")
def generate_prompt(data: PromptRequest):
    user_input = data.text
    
    # Abhi dummy AI logic (baad me real AI add karenge)
    improved_prompt = f"✨ Professional Version:\n{user_input.capitalize()} in a clear and structured way."
    
    return {"result": improved_prompt}