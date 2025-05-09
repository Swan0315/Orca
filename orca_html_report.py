# orca_html_report.py
import datetime

def generate_html_report():
    try:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        html = f"""
        <html>
            <head><title>Orca 시스템 상태</title></head>
            <body>
                <h1>Orca HTML 상태 리포트</h1>
                <p>생성 시각: {now}</p>
                <p>이곳에 시스템 상태 정보를 추가로 넣을 수 있어요.</p>
            </body>
        </html>
        """
        with open(f"orca_system_report_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("📄 HTML 리포트 생성 완료!")
    except Exception as e:
        print(f"⚠ HTML 리포트 생성 실패: {e}")
