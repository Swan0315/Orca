import requests
import os
import time
import threading
import subprocess
import datetime

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
        "6. 실행 과정 로그 기능"
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
            with open("orca_temp.py", "wb") as f:
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

# 오르카 주기 루프 (1시간마다 자동)
def auto_main_loop():
    while True:
        suggest_feature()
        update_orca()
        git_auto_push()
        time.sleep(3600)

# 실행 시작
if __name__ == "__main__":
    threading.Thread(target=auto_main_loop, daemon=True).start()
    while True:
        time.sleep(1)

print("Hello Orca")

def log_system_status(cpu_usage, memory_usage):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("orca_log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{now}] CPU: {cpu_usage:.1f}% / 메모리: {memory_usage:.1f}%\n")

def print_system_status():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    print(f"📊 현재 상태: CPU {cpu:.1f}%, 메모리 {memory:.1f}%")
    log_system_status(cpu, memory)

def auto_main_loop():
    while True:
        suggest_feature()
        update_orca()
        git_auto_push()
        print_system_status()
        time.sleep(3600)

# 자동 명령어 실행 시스템
import subprocess

# 명령어 사전 등록
command_dict = {
    "check_cpu": "wmic cpu get loadpercentage",
    "check_memory": "systeminfo | findstr /C:Memory",
    "check_disk": "wmic diskdrive get status"
}

# 사용자 입력 감지 및 자동 실행
def run_command(command):
    if command in command_dict:
        try:
            print(f"💻 명령어 실행: {command}")
            result = subprocess.check_output(command_dict[command], shell=True).decode()
            print(f"📜 실행 결과: {result}")
            with open("command.log.txt", "a", encoding="utf-8") as f:
                f.write(f"{command} - {result}\n")
        except Exception as e:
            print(f"❌ 명령어 실행 중 오류 발생: {e}")
    else:
        print("⚠️ 알 수 없는 명령어입니다.")

# 실행 예시 (실시간으로 자동 실행)
def auto_command_loop():
    while True:
        user_input = input("명령어를 입력해주세요 (예: check_cpu, check_memory, check_disk): ")
        if user_input in command_dict:
            run_command(user_input)
        else:
            print("⚠️ 알 수 없는 명령어입니다.")

# 실행 시작
if __name__ == "__main__":
    threading.Thread(target=auto_command_loop, daemon=True).start()
    while True:
        time.sleep(1)

# 📁 시스템 정보 수집 기능
import platform
import socket

# 시스템 정보 출력 함수
def print_system_info():
    print("\n🧠 시스템 정보 수집 중...")
    try:
        system_info = {
            "운영체제": platform.system(),
            "OS 버전": platform.version(),
            "컴퓨터 이름": socket.gethostname(),
            "프로세서": platform.processor()
        }
        for key, value in system_info.items():
            print(f"{key}: {value}")
        
        # 로그 파일에 저장
        with open("orca_log.txt", "a", encoding="utf-8") as f:
            f.write("\n[시스템 정보 수집 결과]\n")
            for key, value in system_info.items():
                f.write(f"{key}: {value}\n")
    except Exception as e:
        print(f"❌ 시스템 정보 수집 중 오류 발생: {e}")


# 📁 명령 실행 시 오디오 피드백 추가
import winsound

def play_feedback():
    frequency = 600  # Hz
    duration = 150   # ms
    winsound.Beep(frequency, duration)


# 📁 오르카 상태 로깅 개선
from datetime import datetime

def log_orca_status(message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("orca_log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{now}] {message}\n")
