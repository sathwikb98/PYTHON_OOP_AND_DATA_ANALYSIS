#!/usr/bin/env python3
"""
2.Write a Python script that analyzes a text file containing student grades and generates a comprehensive report. (7 marks)
Input CSV Format:
csv
StudentID,Name,Math,Physics,Chemistry,Biology
S001,Alice Johnson,85,90,88,92
S002,Bob Smith,78,82,75,80
S003,Carol White,92,88,95,90
S004,David Brown,70,68,72,75
Requirements:
  Read the CSV file
  Create a class Student to store each student's information
  Calculate individual student averages
  Generate a report showing: 
o Total number of students
o Class average for each subject
o Overall class average
o Top 3 students by overall average
o Students who scored above 90 in any subject
o Subject-wise highest and lowest scores
  Handle file not found exceptions
  Write formatted output to a text file
"""

import csv

class Student:
    def __init__(self, student_id, name, math, physics, chemistry, biology):
        self.student_id = student_id
        self.name = name
        self.math = int(math)
        self.physics = int(physics)
        self.chemistry = int(chemistry)
        self.biology = int(biology)

    def average(self):
        return (self.math + self.physics + self.chemistry + self.biology) / 4


def analyze_grades(input_file, output_file):
    students = [] # Total students encapsulated inside this.... 

    try:
        with open(input_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = Student(
                    row['StudentID'],
                    row['Name'],
                    row['Math'],
                    row['Physics'],
                    row['Chemistry'],
                    row['Biology']
                )
                students.append(student)

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return

    if not students:
        print("No student data found.")
        return

    # Total students
    total_students = len(students)

    # Subject-wise calculations
    subjects = ['math', 'physics', 'chemistry', 'biology']
    subject_totals = {sub: 0 for sub in subjects}
    subject_highest = {sub: -1 for sub in subjects}
    subject_lowest = {sub: 101 for sub in subjects}

    for student in students:
        for sub in subjects:
            score = getattr(student, sub)
            subject_totals[sub] += score
            subject_highest[sub] = max(subject_highest[sub], score)
            subject_lowest[sub] = min(subject_lowest[sub], score)

    class_avg_subject = {sub: subject_totals[sub] / total_students for sub in subjects}

    # Overall class average
    overall_class_avg = sum(s.average() for s in students) / total_students

    # Top 3 students
    top_3 = sorted(students, key=lambda s: s.average(), reverse=True)[:3]

    # Students scoring above 90 in any subject
    above_90_students = [
        s for s in students
        if any(getattr(s, sub) > 90 for sub in subjects)
    ]

    # report generation.....
    with open(output_file, 'w') as report:
        report.write("===== STUDENT GRADE REPORT =====\n\n")

        report.write(f"Total Students: {total_students}\n\n")

        report.write("Class Average per Subject:\n")
        for sub in subjects:
            report.write(f"  {sub.capitalize()}: {class_avg_subject[sub]:.2f}\n")

        report.write(f"\nOverall Class Average: {overall_class_avg:.2f}\n\n")

        report.write("Top 3 Students by Average:\n")
        for student in top_3:
            report.write(f"  {student.name} ({student.student_id}) - {student.average():.2f}\n")

        report.write("\nStudents Scoring Above 90 in Any Subject:\n")
        for student in above_90_students:
            report.write(f"  {student.name} ({student.student_id})\n")

        report.write("\nSubject-wise Highest and Lowest Scores:\n")
        for sub in subjects:
            report.write(
                f"  {sub.capitalize()} - Highest: {subject_highest[sub]}, "
                f"Lowest: {subject_lowest[sub]}\n"
            )

    print(f"Report successfully generated: {output_file}")


# Run the function
analyze_grades("doc/students.csv", "doc/report.txt")
