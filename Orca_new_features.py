import requests
import os
import time
import threading
import subprocess
import datetime
import psutil  # 시스템 모니터링을 위한 라이브러리 추가

# 최신 버전 py 다운로드 링크 (GitHub 토큰 포함)
py_download_url = "https://raw.githubusercontent.com/Swan0315/Orca/main/orca.py?token=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"

# 기능 제안
def suggest_feature():
    features = [
        "1. 오르카의 성능 최적화",
        "2. 새로운 대화 기능 추가",
        "3. 장기적인 업데이트 및 부가 시스템 도입",
        "4. 나만의 명령어 시스템 추가",
        "5. 실시간 시스템 모니터링 기능"
    ]
    print("💡 오르카가 제안하는 기능 목록:")
    for feature in features:
        print(" -", feature)

# 시스템 모니터링 기능 추가
def monitor_system():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    print(f"""📊 현재 시스템 상태 확인 중...
CPU 사용량: {cpu_usage}%
메모리 사용량: {memory_usage}%""")

# 업데이트 확인 및 반영
def update_orca():
    print("🔄 Orca: 업데이트 확인 중…")
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
        monitor_system()  # 시스템 모니터링 추가
        update_orca()
        git_auto_push()
        time.sleep(3600)

# 실행 시작
if __name__ == "__main__":
    threading.Thread(target=auto_main_loop, daemon=True).start()
    while True:
        time.sleep(1)

print("Hello Orca")
