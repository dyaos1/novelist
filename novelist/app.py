from fastapi import FastAPI
from openai import OpenAI

from pydantic import BaseModel
from dotenv import load_dotenv
import os
from typing import List, Dict

# 변수
load_dotenv()

client = OpenAI()
# client = OpenAI(os.getenv("OPENAI_API_KEY"))

app = FastAPI()

# 함수
class UserRequest(BaseModel):
    genre: str = "thriller"
    characters: List[Dict[str, str]] = [{"슈카":"경제유투버"}]
    news_text: str = """기름값 하락 계속…휘발유 6.6원·경유 5.9원↓ 이번 주에도 국내 주유소 휘발유와 경유 판매 가격이 동반 하락했습니다.
한국석유공사 유가정보시스템 오피넷에 따르면 6월 셋째주 전국 주유소 휘발유 평균 판매 가격은 전주보다 6.6원 하락한 리터당 1,575.8원을 기록했습니다.
경유 판매 가격 역시 8.7원 내린 1,387.6원으로 집계됐습니다.
휘발유 가격은 8주째, 경유 가격은 9주 연속 내림세입니다.
대한석유협회 관계자는 "다음 주에도 휘발유·경유 가격은 하향 안정세를 보이겠지만, 그 다음 주부터는 특히 경유 가격이 반등할 가능성이 있다"고 전망했습니다."""

def readTemplate(filePath: str) -> str :
    with open(filePath, "r") as f:
        prompt_template = f.read()

    return prompt_template

def openAIRequest(
    prompt: str,
    model: str = "gpt-3.5-turbo",
    max_token:int = 500,
    temperature: float = 0.8
):
    completion = client.chat.completions.create(
    model=model,
    max_tokens=max_token,
    temperature=temperature,
    messages=[
        {"role": "user", "content": prompt}
    ]
    )

    return completion.choices[0].message

# FastApi
@app.post("/write")
def writer(req: UserRequest) -> Dict[str, str]:
    prompt_template = readTemplate("./novelist/template.txt")
    prompt = prompt_template.format(
        genre = req.genre,
        characters = req.characters,
        news_text = req.news_text
    )
    result = openAIRequest(prompt)

    return {"result": result}

@app.get("/")
def read_root():
    message = ""
    return {"Hello": "World", "message": message}

# 실행
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
