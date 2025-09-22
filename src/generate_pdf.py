from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

def main():
    c = canvas.Canvas("reports/report.pdf", pagesize=A4)
    w, h = A4

    c.setFont("Helvetica-Bold", 18)
    c.drawString(72, h-72, "자동 생성 분석 보고서")

    c.setFont("Helvetica", 12)
    c.drawString(72, h-110, f"생성 시각: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    c.drawString(72, h-140, "이 PDF는 GitHub Actions에서 자동 생성되었습니다.")

    c.showPage()
    c.save()

if __name__ == "__main__":
    main()
