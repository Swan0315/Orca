
import openai
import datetime
import os

# GPT API 키를 아래에 입력하세요
openai.api_key = "YOUR_API_KEY"

# GPT에게 질문하고 응답을 받아오는 함수
def ask_gpt(question, save_as="orca_response.py"):
    print(f"📤 GPT에게 질문 중: {question}")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "너는 Orca라는 이름의 AI 보조야. 사용자의 시스템 자동화를 돕고 개선하는 코드만 작성해줘."},
                {"role": "user", "content": question}
            ]
        )
        answer = response.choices[0].message.content
        with open(save_as, "w", encoding="utf-8") as f:
            f.write(answer)
        print(f"✅ GPT 응답 저장 완료: {save_as}")
    except Exception as e:
        print(f"❌ GPT 요청 실패: {e}")

# 예시 사용
if __name__ == "__main__":
    ask_gpt("오르카가 시스템 디스크 사용량을 점검하고 경고하도록 자동화 코드를 짜줘.")
