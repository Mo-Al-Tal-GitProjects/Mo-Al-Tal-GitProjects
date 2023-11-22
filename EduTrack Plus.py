import pandas as pd
import matplotlib.pyplot as plt

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
        self.study_times = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def add_study_time(self, time):
        self.study_times.append(time)

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def get_total_study_time(self):
        return sum(self.study_times)

def save_student_data(student, file_name='students.csv'):
    try:
        df = pd.read_csv(file_name)
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Name', 'Grades', 'Study Times'])

    new_data = {'Name': student.name, 'Grades': student.grades, 'Study Times': student.study_times}
    df = df.append(new_data, ignore_index=True)
    df.to_csv(file_name, index=False)

def add_student_data(student):
    while True:
        grade = input(f"Enter grade for {student.name} (or 'done' to finish): ")
        if grade.lower() == 'done':
            break
        try:
            student.add_grade(float(grade))
        except ValueError:
            print("Invalid input. Please enter a numeric grade.")

    while True:
        time = input(f"Enter study time for {student.name} in hours (or 'done' to finish): ")
        if time.lower() == 'done':
            break
        try:
            student.add_study_time(float(time))
        except ValueError:
            print("Invalid input. Please enter a numeric time.")
    

def plot_grade_distribution(student):
    plt.hist(student.grades, bins=10, alpha=0.7)
    plt.title(f"Grade Distribution for {student.name}")
    plt.xlabel("Grades")
    plt.ylabel("Frequency")
    plt.show()

def main():
    print("Welcome to the Educational Progress Tracker")
    student_name = input("Enter the student's name: ")
    student = Student(student_name)

    add_student_data(student)
    save_student_data(student)

    print(f"Average Grade: {student.get_average_grade()}")
    print(f"Total Study Time: {student.get_total_study_time()} hours")

    plot_grade_distribution(student)

if __name__ == "__main__":
    main()
