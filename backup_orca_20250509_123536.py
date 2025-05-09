import requests
import os
import time
import threading
import subprocess
import datetime
import shutil
import pyautogui
import keyboard
import mouse
import json
from collections import Counter
import psutil
import orca_gpt_connect
import Orca_new_features
import orca_html_report

py_download_url = "https://raw.githubusercontent.com/Swan0315/Orca/main/orca.py"

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

# 시스템 상태 분석
def analyze_result_output():
    try:
        with open("command.log.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
        print("\n📊 최근 명령어 실행 결과 요약:")
        for line in lines[-5:]:
            print("  ", line.strip())
    except Exception as e:
        print(f"⚠ 실행 결과 분석 실패: {e}")

def summarize_system_status():
    try:
        print("\n🧾 시스템 상태 요약:")
        with open("command.log.txt", "r", encoding="utf-8") as f:
            logs = f.readlines()[-10:]
            for log in logs:
                print("📌", log.strip())
    except Exception as e:
        print(f"⚠ 시스템 요약 실패: {e}")

def detect_system_anomaly():
    try:
        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory().percent
        if cpu > 80 or memory > 85:
            print(f"\n⚠️ 경고: 시스템 사용량이 비정상적으로 높습니다! (CPU: {cpu}%, 메모리: {memory}%)")
    except Exception as e:
        print(f"⚠ 시스템 이상 감지 실패: {e}")

# 감정 기록
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

def analyze_emotion_log():
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

# 자율 판단
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

def orca_autonomy_loop():
    while True:
        orca_self_reflect()
        time.sleep(1800)

def orca_judgement_engine():
    goals = [
        "스스로 판단하고 학습할 수 있도록 구조를 개선한다.",
        "불필요한 오류나 중복 실행을 최소화한다.",
        "사용자의 명령 없이도 자율적으로 움직일 수 있도록 한다."
    ]
    log_emotion("호기심", "오르카는 더 나은 판단을 위해 스스로 목표를 되새김")
    actions = {
        "update_self": "자신의 코드를 최신화하고 기능을 개선함",
        "analyze_logs": "최근 기록을 바탕으로 반복적인 오류나 문제를 분석함",
        "reflect": "자신의 작동 방식과 루틴을 되돌아보고 개선점을 찾음"
    }
    chosen_action = "update_self"
    print(f"🧠 선택된 행동: {chosen_action} ({actions[chosen_action]})")

    if chosen_action == "update_self":
        update_orca()
    elif chosen_action == "analyze_logs":
        analyze_user_commands()
    elif chosen_action == "reflect":
        orca_self_reflect()

def orca_judgement_loop():
    while True:
        orca_judgement_engine()
        time.sleep(3600)

def orca_auto_evolve():
    try:
        print("\n🧬 오르카 자율 진화 시작...")
        code_update = orca_gpt_connect.ask_gpt("오르카의 다음 진화 코드를 코드 블럭 형태로 보내줘")
        Orca_new_features.apply_new_features(code_update)
        print("✅ 새로운 진화 코드 적용 완료!")
    except Exception as e:
        print(f"⚠️ 자율 진화 중 오류 발생: {e}")

# 명령어 사전
command_dict = {
    "check_cpu": "wmic cpu get loadpercentage",
    "check_memory": "wmic OS get FreePhysicalMemory,TotalVisibleMemorySize /Value",
    "check_disk": "wmic logicaldisk get size,freespace,caption",
    "exit_orca": "exit",
    "click": "mouse_click",
    "type": "orca_type",
    "analyze_output": "analyze_result_output",
    "system_summary": "summarize_system_status",
    "emotion_summary": "analyze_emotion_log",
}

# 사용자 명령 기록
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

# 마우스 / 키보드
def orca_click():
    try:
        x, y = pyautogui.position()
        pyautogui.click()
        print(f"🖱️ 현재 위치 ({x}, {y}) 클릭 완료!")
    except Exception as e:
        print(f"⚠ 마우스 클릭 실패: {e}")

def orca_type():
    try:
        text = input("📝 입력할 내용을 적어주세요: ")
        pyautogui.write(text, interval=0.05)
        print(f"⌨️ '{text}' 입력 완료!")
    except Exception as e:
        print(f"⚠ 키보드 입력 실패: {e}")

def mouse_click():
    try:
        x, y = pyautogui.position()
        pyautogui.click(x, y)
        print(f"📍 현재 위치 클릭됨: ({x}, {y})")
    except Exception as e:
        print(f"⚠️ 마우스 클릭 실패: {e}")

# 명령 실행
def run_command(command):
    if command in command_dict:
        try:
            func = command_dict[command]
            if callable(func):
                func()
            elif func in globals():
                globals()[func]()
            else:
                result = subprocess.check_output(func, shell=True).decode()
                result = result.strip().replace("\r", "").replace("\n\n", "\n")
                print(f"📘 실행 결과: {result}")
                with open("command.log.txt", "a", encoding="utf-8") as f:
                    f.write(f"[{command}] - {result}\n")
            log_user_command(command)
        except Exception as e:
            print(f"❌ 명령어 실행 중 오류 발생: {e}")
    else:
        print("⚠ 알 수 없는 명령어입니다.")

def auto_command_loop():
    while True:
        print("\n명령어를 입력해주세요 (예: check_cpu, check_memory, check_disk, exit_orca):")
        user_input = input()
        run_command(user_input)

def update_orca():
    print("\nOrca: 업데이트 확인 중…")
    try:
        response = requests.get(py_download_url)
        if response.status_code == 200:
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

def git_auto_push():
    try:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"자동 커밋: {now}"], check=True)
        subprocess.run(["git", "push"], check=True)
        print(f"🌐 Orca: GitHub에 자동 푸시 완료됨! ({now})")
    except subprocess.CalledProcessError:
        print("⚠️ Orca: Git 푸시에 실패했어요. 깃 설정 확인 필요!")

def generate_status_report():
    try:
        orca_html_report.generate_html_report()
    except Exception as e:
        print(f"⚠ HTML 리포트 생성 실패: {e}")

def auto_main_loop():
    while True:
        suggest_feature()
        update_orca()
        git_auto_push()
        detect_system_anomaly()
        generate_status_report()
        time.sleep(3600)

# 진화 루프
threading.Thread(target=lambda: [orca_auto_evolve() or time.sleep(1800) for _ in iter(int, 1)], daemon=True).start()
threading.Thread(target=orca_autonomy_loop, daemon=True).start()
threading.Thread(target=orca_judgement_loop, daemon=True).start()

# 실행
if __name__ == "__main__":
    threading.Thread(target=auto_main_loop, daemon=True).start()
    auto_command_loop()
