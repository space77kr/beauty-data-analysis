from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase import pdfmetrics
from datetime import datetime
import os

def main():
    os.makedirs("reports", exist_ok=True)

    c = canvas.Canvas("reports/report.pdf", pagesize=A4)
    w, h = A4

    # 한글 폰트 등록
    pdfmetrics.registerFont(UnicodeCIDFont("HYSMyeongJo-Medium"))

    c.setFont("HYSMyeongJo-Medium", 18)
    c.drawString(72, h-72, "자동 생성 분석 보고서")

    c.setFont("HYSMyeongJo-Medium", 12)
    c.drawString(72, h-110, f"생성 시각: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    c.drawString(72, h-140, "이 PDF는 GitHub Actions에서 자동 생성되었습니다.")

    # 페이지 번호 예시
    c.setFont("Helvetica", 10)
    c.drawRightString(w-72, 36, "Page 1")

    c.showPage()
    c.save()

if __name__ == "__main__":
    main()
