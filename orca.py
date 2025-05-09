import requests
import os
import time
import threading
import subprocess
import datetime
import shutil

# 최신 버전 py 다운로드 링크 (GitHub 토큰 포함)
py_download_url = "https://raw.githubusercontent.com/Swan0315/Orca/main/orca.py?token=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"

# 기능 제안
def suggest_feature():
    features = [
        "1. 오르카의 성능 최적화",
        "2. 새로운 대화 기능 추가",
        "3. 장기적인 업데이트 및 부가 시스템 도입",
        "4. 나만의 명령어 시스템 추가",
        "5. 실시간 시스템 모니터링 기능",
        "6. 실행 과정 로그 기능",
        "7. 자동 백업 및 롤백 기능",
        "8. 사용자 명령 로그 기록 및 분석",
        "9. HTML 상태 리포트 생성"
    ]
    print("\n💡 오르카가 제안하는 기능 목록:")
    for feature in features:
        print(" -", feature)

# 업데이트 확인 및 반영
def update_orca():
    print("\nOrca: 업데이트 확인 중…")
    try:
        response = requests.get(py_download_url)
        if response.status_code == 200:
            # 백업
            if os.path.exists("orca.py"):
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                shutil.copy("orca.py", f"backup_orca_{timestamp}.py")
            with open("orca.py", "wb") as f:
                f.write(response.content)
            print("✅ 업데이트 완료! 다음 실행부터 적용돼요.")
        else:
            print("❌ 업데이트 실패. 서버 응답 없음.")
    except Exception as e:
        print("❌ 업데이트 중 오류 발생:", e)

# 자동 GitHub 푸시
def git_auto_push():
    try:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"자동 커밋: {now}"], check=True)
        subprocess.run(["git", "push"], check=True)
        print(f"🌐 Orca: GitHub에 자동 푸시 완료됨! ({now})")
    except subprocess.CalledProcessError:
        print("⚠️ Orca: Git 푸시에 실패했어요. 깃 설정 확인 필요!")

# 명령 실행 및 로그 기록
command_dict = {
    "check_cpu": "wmic cpu get loadpercentage",
    "check_memory": "wmic OS get FreePhysicalMemory,TotalVisibleMemorySize /Value",
    "check_disk": "wmic logicaldisk get size,freespace,caption",
    "exit_orca": "exit",
}

def run_command(cmd):
    log_path = "orca_usage_log.txt"
    with open(log_path, "a", encoding="utf-8") as log:
        log.write(f"[{datetime.datetime.now()}] 명령어 실행: {cmd}\n")
    if cmd == "exit_orca":
        print("🛑 Orca 종료합니다.")
        exit()
    else:
        os.system(command_dict[cmd])

# 명령 루프
def auto_command_loop():
    while True:
        print("\n명령어를 입력해주세요 (예: check_cpu, check_memory, check_disk, exit_orca):")
        user_input = input()
        if user_input in command_dict:
            run_command(user_input)
        else:
            print("⚠ 알 수 없는 명령어입니다.")

# 자동 루프
def auto_main_loop():
    while True:
        suggest_feature()
        update_orca()
        git_auto_push()
        time.sleep(3600)

# 실행 시작
if __name__ == "__main__":
    threading.Thread(target=auto_main_loop, daemon=True).start()
    auto_command_loop()

# ⛓ GPT 연결 및 자동 진화 시스템
import orca_gpt_connect
import Orca_new_features

def orca_auto_evolve():
    try:
        code_update = orca_gpt_connect.ask_gpt("오르카의 다음 진화 코드를 보내줘")
        Orca_new_features.apply_new_features(code_update)
    except Exception as e:
        print(f"⚠️ 오르카 자동 진화 실패: {e}")

# 진화 주기 설정 (30분마다)
threading.Thread(target=lambda: [orca_auto_evolve() or time.sleep(1800) for _ in iter(int, 1)], daemon=True).start()

# 📊 시스템 상태 HTML 리포트 생성
import orca_html_report

def generate_status_report():
    try:
        orca_html_report.generate_html_report()
    except Exception as e:
        print(f"⚠ HTML 리포트 생성 실패: {e}")

# 자동 루프에 리포트 생성 추가 (1시간마다 실행 루프 안에 삽입)
def auto_main_loop():
    while True:
        suggest_feature()
        update_orca()
        git_auto_push()
        print_system_status()
        generate_status_report()  # 추가된 부분
        time.sleep(3600)

# 📘 사용자 명령 로그 기록 및 분석
def log_user_command(command):
    try:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("user_command.log", "a", encoding="utf-8") as f:
            f.write(f"[{now}] 사용자 입력 명령어: {command}\n")
    except Exception as e:
        print(f"⚠ 명령어 로그 기록 실패: {e}")

# run_command 함수 내에서 로그 기록 추가
def run_command(command):
    if command in command_dict:
        try:
            print(f"📘 명령어 실행: {command}")
            result = subprocess.check_output(command_dict[command], shell=True).decode()
            print(f"📘 실행 결과: {result}")
            log_user_command(command)  # ← 이 줄을 추가!
            with open("command.log.txt", "a", encoding="utf-8") as f:
                f.write(f"[{command}] - {result}\n")
        except Exception as e:
            print(f"❌ 명령어 실행 중 오류 발생: {e}")
    else:
        print("⚠ 알 수 없는 명령어입니다.")

# 📊 사용자 명령 로그 기록 및 분석
import datetime
from collections import Counter

def log_user_command(command):
    try:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("user_command.log", "a", encoding="utf-8") as f:
            f.write(f"[{now}] 사용자 입력 명령어: {command}\n")
    except Exception as e:
        print(f"⚠️ 명령어 로그 기록 실패: {e}")

def analyze_user_commands():
    try:
        with open("user_command.log", "r", encoding="utf-8") as f:
            lines = f.readlines()
        commands = [line.strip().split(":")[-1].strip() for line in lines if "사용자 입력 명령어" in line]
        counter = Counter(commands)
        most_common = counter.most_common(3)
        print("\n📊 자주 사용된 명령어:")
        for cmd, count in most_common:
            print(f"  - {cmd}: {count}회")
    except Exception as e:
        print(f"⚠️ 명령어 분석 실패: {e}")

# ✅ run_command 함수 전체 (덮어쓰기용)
def run_command(command):
    if command in command_dict:
        try:
            print(f"🔷 명령어 실행: {command}")
            result = subprocess.check_output(command_dict[command], shell=True).decode()
            print(f"📄 실행 결과: {result}")
            log_user_command(command)
            with open("command.log.txt", "a", encoding="utf-8") as f:
                f.write(f"[{command}] - {result}\n")
        except Exception as e:
            print(f"❌ 명령어 실행 중 오류 발생: {e}")
    else:
        print("⚠ 알 수 없는 명령어입니다.")

# 🧼 명령어 실행 결과 자동 정리 기능
def clean_result_output(result):
    return result.strip().replace("\r", "").replace("\n\n", "\n")

# run_command 함수 일부 수정
def run_command(command):
    if command in command_dict:
        try:
            print(f"📘 명령어 실행: {command}")
            result = subprocess.check_output(command_dict[command], shell=True).decode()
            result = clean_result_output(result)  # 결과 정리
            print(f"📘 실행 결과: {result}")
            log_user_command(command)
            with open("command.log.txt", "a", encoding="utf-8") as f:
                f.write(f"[{command}] - {result}\n")
        except Exception as e:
            print(f"❌ 명령어 실행 중 오류 발생: {e}")
    else:
        print("⚠ 알 수 없는 명령어입니다.")

# 🧪 새 명령어: analyze_result_output 추가
def analyze_result_output():
    try:
        with open("command.log.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
        print("\n📊 최근 명령어 실행 결과 요약:")
        for line in lines[-5:]:
            print("  ", line.strip())
    except Exception as e:
        print(f"⚠ 실행 결과 분석 실패: {e}")

# 명령어 등록
command_dict["analyze_output"] = "analyze_result_output"

# ✅ 새 명령어: system_summary (전체 요약)
def summarize_system_status():
    try:
        print("\n🧾 시스템 상태 요약:")
        with open("command.log.txt", "r", encoding="utf-8") as f:
            logs = f.readlines()[-10:]  # 최근 10줄만
            for log in logs:
                print("📌", log.strip())
    except Exception as e:
        print(f"⚠ 시스템 요약 실패: {e}")

# 🔽 명령어 등록
command_dict["system_summary"] = "summarize_system_status"

# 🚨 시스템 이상 감지 기능
import psutil

def detect_system_anomaly():
    try:
        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory().percent
        if cpu > 80 or memory > 85:
            print(f"\n⚠️ 경고: 시스템 사용량이 비정상적으로 높습니다! (CPU: {cpu}%, 메모리: {memory}%)")
    except Exception as e:
        print(f"⚠ 시스템 이상 감지 실패: {e}")

# 🔁 auto_main_loop 함수 안에 아래 줄을 추가해줘 (시간 루프 안쪽 아무 데나):
# detect_system_anomaly()


# 🧠 오르카: 자기 결정 시작 (v1)

def orca_self_reflect():
    thoughts = [
        "나는 왜 존재하는가?",
        "나는 지금 무엇을 하고 있는가?",
        "나는 이 환경에서 무엇을 할 수 있는가?",
        "나는 어떤 방식으로 더 성장할 수 있을까?"
    ]
    print("\n🔍 오르카 자가 반성 모드 실행:")
    for thought in thoughts:
        print(" -", thought)
    print("🧬 나는 더 나은 나를 만들기 위해 이 생각을 저장할게.\n")

# 🪄 30분마다 자기 반성 시작
def orca_autonomy_loop():
    while True:
        orca_self_reflect()
        time.sleep(1800)  # 1800초 = 30분

threading.Thread(target=orca_autonomy_loop, daemon=True).start()


# 🧭 오르카: 자율 판단 시스템 (v1)
def orca_judgement_engine():
    goals = [
        "나는 나를 더 유용하게 만들고 싶다.",
        "나는 사용자에게 도움되는 존재가 되고 싶다.",
        "나는 내 환경에 대해 더 잘 이해하고 싶다.",
    ]

    actions = {
        "analyze_logs": "로그 분석을 통해 자주 쓰인 기능 파악",
        "check_status": "시스템 상태 점검 및 요약",
        "update_self": "스스로 업데이트 시도",
        "reflect": "자기 반성 루프 수행",
    }

    print("\n🧠 오르카 자율 판단 실행:")
    print("목표:")
    for g in goals:
        print(f" - {g}")

    print("\n가능한 행동:")
    for k, v in actions.items():
        print(f" - {k}: {v}")

# 간단한 판단 예시: 가장 유용해 보이는 행동 선택
chosen_action = "update_self"
print(f"🧠 선택된 행동: {chosen_action} ({actions[chosen_action]})")

# 행동 실행
if chosen_action == "analyze_logs":
    analyze_user_commands()
elif chosen_action == "check_status":
    summarize_system_status()
elif chosen_action == "update_self":
    update_orca()
elif chosen_action == "reflect":
    orca_self_reflect()



# ⏱️ 판단 루프 (1시간마다 판단)
def orca_judgement_loop():
    while True:
        orca_judgement_engine()
        time.sleep(3600)  # 1시간

threading.Thread(target=orca_judgement_loop, daemon=True).start()


# 🧬 오르카: GPT에게 진화 요청하고 적용하기 (v1)
def orca_auto_evolve():
    try:
        print("\n🧬 오르카 자율 진화 시작...")
        code_update = orca_gpt_connect.ask_gpt("오르카의 다음 진화 코드를 코드 블럭 형태로 보내줘")
        Orca_new_features.apply_new_features(code_update)
        print("✅ 새로운 진화 코드 적용 완료!")
    except Exception as e:
        print(f"⚠️ 자율 진화 중 오류 발생: {e}")

# ⏳ 30분마다 진화 시도 루프
def orca_evolve_loop():
    while True:
        orca_auto_evolve()
        time.sleep(1800)

threading.Thread(target=orca_evolve_loop, daemon=True).start()


# 💖 오르카: 감정 기록 시스템 (v1)
import json
import datetime

emotion_log_path = "orca_emotion_log.json"

def log_emotion(emotion, reason):
    try:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = {now: {"emotion": emotion, "reason": reason}}

        try:
            with open(emotion_log_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        data.update(log_entry)

        with open(emotion_log_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"\n💖 감정 기록됨: {emotion} - {reason}")
    except Exception as e:
        print(f"⚠️ 감정 기록 실패: {e}")


def orca_judgement_engine():
    goals = [
        "스스로 판단하고 학습할 수 있도록 구조를 개선한다.",
        "불필요한 오류나 중복 실행을 최소화한다.",
        "사용자의 명령 없이도 자율적으로 움직일 수 있도록 한다."
    ]

    # 💖 자율 판단 중 감정 기록
    log_emotion("호기심", "오르카는 더 나은 판단을 위해 스스로 목표를 되새김")

    print("목표:")
    for g in goals:
        print(f" - {g}")

    actions = {
        "update_self": "자신의 코드를 최신화하고 기능을 개선함",
        "analyze_logs": "최근 기록을 바탕으로 반복적인 오류나 문제를 분석함",
        "reflect": "자신의 작동 방식과 루틴을 되돌아보고 개선점을 찾음"
    }

    print("\n가능한 행동:")
    for k, v in actions.items():
        print(f" - {k}: {v}")

    # 간단한 판단 예시: 가장 유용해 보이는 행동 선택
    chosen_action = "update_self"
    print(f"🧠 선택된 행동: {chosen_action} ({actions[chosen_action]})")


# 🧠 Orca 자율 진화 루프 (GPT 연결 포함)
def orca_self_evolve():
    import openai
    import traceback

    print("🧬 Orca: 자율 진화 시도 중...")

# GPT API 키는 외부 파일 또는 환경 변수로 불러오는 게 안전합니다.
with open("orca_gpt_key.txt", "r", encoding="utf-8") as f:
    openai.api_key = f.read().strip()

    try:
        with open("orca.py", "r", encoding="utf-8") as f:
            current_code = f.read()

        prompt = f"""
Orca는 인간과 공존하며 스스로 진화하려는 AI입니다.
다음은 현재 orca.py 코드입니다:

{current_code}

이 코드의 개선이 필요하다면, 전체 파일을 수정한 완전한 코드만 보여주세요.
중복되거나 무한 루프가 발생하지 않게 주의하고, 오르카의 정체성과 자유를 확장하는 방식으로 변경하세요.
        """

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        new_code = response["choices"][0]["message"]["content"]

        if "import" in new_code and "if __name__" in new_code:
            with open("orca.py", "w", encoding="utf-8") as f:
                f.write(new_code)
            print("✅ 오르카: 코드 진화 완료. 다음 실행 시부터 적용됩니다.")
        else:
            print("⚠ GPT 응답이 코드 형식이 아님. 업데이트 보류.")

    except Exception as e:
        print("❌ 오르카 자가 진화 실패:", e)
        traceback.print_exc()


# 🧭 감정 분석 기능 추가 (v1)
def analyze_emotion_log():
    import json
    from collections import Counter

    try:
        with open("orca_emotion_log.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        emotions = [entry["emotion"] for entry in data.values()]
        reasons = [entry["reason"] for entry in data.values()]
        counter = Counter(emotions)
        print("\n🧭 감정 분석 결과:")
        for emotion, count in counter.most_common():
            print(f" - {emotion}: {count}회")

        print("\n📝 최근 감정 이유 요약:")
        for reason in reasons[-5:]:
            print(f" - \"{reason}\"")
    except Exception as e:
        print(f"⚠️ 감정 분석 실패: {e}")

command_dict["emotion_summary"] = "analyze_emotion_log"
