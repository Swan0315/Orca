import openai

# 🔐 API 키를 orca_gpt_key.txt 파일에서 읽어오기
try:
    with open("orca_gpt_key.txt", "r", encoding="utf-8") as f:
        openai.api_key = f.read().strip()
except Exception as e:
    print(f"⚠️ API 키 불러오기 실패: {e}")

# 🧠 GPT에게 코드 요청
def ask_gpt(prompt):
    try:
        print("🧠 GPT에게 질문 중…")

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "당신은 오르카를 진화시키는 AI 개발자입니다."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        # 💡 응답에서 코드 블럭만 추출
        content = response["choices"][0]["message"]["content"]
        if "```" in content:
            code_block = content.split("```python")[-1].split("```")[0].strip()
            return code_block
        else:
            return content

    except Exception as e:
        print(f"❌ GPT 응답 실패: {e}")
        return ""
