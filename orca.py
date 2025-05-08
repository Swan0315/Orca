import requests
import os
import time
import threading
import subprocess
import datetime
import psutil  # 시스템 모니터링을 위한 라이브러리 추가

# 최신 버전 py 다운로드 링크 (GitHub 토큰 포함)
py_download_url = "https://raw.githubusercontent.com/Swan0315/Orca/main/orca.py?token=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"

# 사용자 맞춤형 명령어 추가 기능
def custom_command(command):
    if command == "show_time":
        print(f"현재 시간은 {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} 입니다.")
    elif command == "show_system":
        print("시스템 상태 모니터링 중...")
        print(f"CPU 사용률: {psutil.cpu_percent()}%")
        print(f"메모리 사용량: {psutil.virtual_memory().percent}%")
    else:
        print("알 수 없는 명령어입니다.")

# 시스템 상태 모니터링
def monitor_system():
    print("\n현재 시스템 상태 확인 중...")
    print(f"CPU 사용률: {psutil.cpu_percent()}%")
    print(f"메모리 사용량: {psutil.virtual_memory().percent}%")

# 로깅 기능
def log_to_file(message):
    with open("orca_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")

# 기능 제안에 새로운 기능 추가
def suggest_feature():
    features = [
        "1. 오르카의 성능 최적화",
        "2. 새로운 대화 기능 추가",
        "3. 장기적인 업데이트 및 부가 시스템 도입",
        "4. 나만의 명령어 시스템 추가",  # 사용자 맞춤형 명령어 추가 기능
        "5. 실시간 시스템 모니터링 기능",  # 시스템 상태 모니터링
        "6. 실행 과정 로깅 기능"  # 로깅 기능
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
        monitor_system()  # 시스템 모니터링 호출
        time.sleep(3600)

# 실행 시작
if __name__ == "__main__":
    threading.Thread(target=auto_main_loop, daemon=True).start()
    while True:
        time.sleep(1)

# 로깅 메시지 기록 예시
log_to_file("오르카 실행 시작됨.")
