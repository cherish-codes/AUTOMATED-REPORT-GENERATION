import csv
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
students = []
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)
total_students = len(students)
marks = [int(s["Marks"]) for s in students]
average_marks = sum(marks) / total_students
highest_marks = max(marks)
c = canvas.Canvas("report.pdf", pagesize=A4)
width, height = A4

y = height - 80  
c.setFont("Helvetica-Bold", 16)
c.drawCentredString(width / 2, y, "STUDENT REPORT")
y -= 20
c.line(40, y, width - 40, y)
y -= 30
c.setFont("Helvetica-Bold", 12)
c.drawString(100, y, "Name")
c.drawString(350, y, "Marks")
y -= 20
c.line(80, y, width - 80, y)
y -= 20
c.setFont("Helvetica", 12)
for s in students:
    c.drawString(100, y, s['Name'])
    c.drawString(350, y, s['Marks'])
    y -= 20
y -= 10
c.line(40, y, width - 40, y)
y -= 30
c.setFont("Helvetica-Bold", 12)
c.drawString(60, y, "Summary:")
y -= 20

c.setFont("Helvetica", 12)
c.drawString(60, y, f"Total Students: {total_students}")
y -= 20
c.drawString(60, y, f"Average Marks: {average_marks:.2f}")
y -= 20
c.drawString(60, y, f"Highest Marks: {highest_marks}")

c.save()

print("PDF Report Generated Successfully!")
