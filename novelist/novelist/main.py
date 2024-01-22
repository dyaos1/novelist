from fastapi import FastAPI
from openai import OpenAI

import os
from typing import List, Dict
from pydantic import BaseModel

client = OpenAI()
app = FastAPI()

class UserRequest(BaseModel):
    genre: str
    # character: List[Dict[str, str]] | None = None
    character: str
    news_text: str

def request_gpt_api(
  prompt: str = "Compose a poem that explains the concept of recursion in programming.",
  model: str = "gpt-3.5-turbo",
  max_token: int = 500,
  temperature: float = 0.8
) -> str:
  response = client.chat.completions.create(
    model=model,
    max_tokens=max_token,
    temperature=temperature,
    messages=[
      {"role": "system", "content": "넌 흥미로운 소설을 쓰는 소설가야."},
      {"role": "user", "content": prompt}
    ]
  )
  print(response.choices[0].message)
  
  return response.choices[0].message

@app.get('/')
def index():
  result = request_gpt_api()
  return {"result": result.content}

@app.post('/writer')
def write(userRequest: UserRequest):
  
  prompt = f"<등장인물>{userRequest.character}</등장인물><뉴스기사> {userRequest.news_text} </뉴스기사> <등장인물>과 <뉴스기사>를 소재로 {userRequest.genre} 소설을 써줘."
  result = request_gpt_api(prompt=prompt)
  return {"result": result.content}
