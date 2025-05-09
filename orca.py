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
