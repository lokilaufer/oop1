class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rate_lectur(self, lectur, course, grades):
        if (isinstance(lectur, Lecturer) and course in lectur.courses_attached and course
                in self.courses_in_progress and grades in range(0,11)):
            if course in lectur.grades:
                lectur.grades[course] += [grades]
            else:
                lectur.grades[course] = [grades]
            lectur.average_grade = lectur.get_average_grade()
        else:
            return 'Ошибка'
    def get_average_grade(self):
        return sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за ДЗ: {self.average_grade}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

    def __lt__(self, other):
        return self.average_grade < other.average_grade

    def __gt__(self, other):
        return self.average_grade > other.average_grade

    def __eq__(self, other):
        return self.average_grade == other.average_grade

    def __ne__(self, other):
        return self.average_grade != other.average_grade
# ------------------------------------------------------------
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
# на основе класса ментор создаем дочерний класс лектор---------

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grade = 0

    def get_average_grade(self):
        return sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_grade}')

    def __lt__(self, other):
        return self.average_grade < other.average_grade

    def __gt__(self, other):
        return self.average_grade > other.average_grade

    def __eq__(self, other):
        return self.average_grade == other.average_grade

    def __ne__(self, other):
        return self.average_grade != other.average_grade

        # на основе класса ментор делаем класс ревьюер -----------------------------------

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if (isinstance(student,
                        Student) and course in self.courses_attached and course in student.courses_in_progress
                and grade in range(0, 11)):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            student.average_grade = student.get_average_grade()
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')
# создаем студентов -----------------------------------------------------------------------------------------
student_1 = Student('Peter', 'Sergeev', 'man')
student_1.courses_in_progress += ['Python', 'Java']

student_2 = Student('Kat', 'Sokolova', 'woman')
student_2.courses_in_progress += ['Python', 'Java']

student_3 = Student('Oksana', 'Kireeva', 'woman')
student_3.courses_in_progress += ['Python', 'Java']
# создаем лекторов --------------------------------------

lecturer_1 = Lecturer('Dmitri', 'Frolov')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Alex', 'Kim')
lecturer_2.courses_attached += ['Java']
# создаем проверяющих --------------------------------

reviewer_1 = Reviewer('Alex', 'Nikolaev')
reviewer_1.courses_attached += ['Python', 'Java']

reviewer_2 = Reviewer('Liza', 'Sokolova')
reviewer_2.courses_attached += ['Python', 'Java']
# выставляем оценки студентам ------------------------
reviewer_1.rate_hw(student_1, 'Python', 11)
reviewer_1.rate_hw(student_1, 'Java', 7)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Java', 8)
reviewer_1.rate_hw(student_3, 'Python', 9)
reviewer_1.rate_hw(student_3, 'Java', 10)

reviewer_2.rate_hw(student_1, 'Python', 6)
reviewer_2.rate_hw(student_1, 'Java', 9)
reviewer_2.rate_hw(student_2, 'Python', 7)
reviewer_2.rate_hw(student_2, 'Java', 11)
reviewer_2.rate_hw(student_3, 'Python', 10)
reviewer_2.rate_hw(student_3, 'Java', 6)
# выставляем оценки лекторам -----------------------------------

student_1.rate_lectur(lecturer_1, 'Python', 11)
student_1.rate_lectur(lecturer_2, 'Java', 11)
student_1.rate_lectur(lecturer_1, 'Python', 8)
student_1.rate_lectur(lecturer_2, 'Java', 8)

student_2.rate_lectur(lecturer_1, 'Python', 11)
student_2.rate_lectur(lecturer_2, 'Java', 7)
student_2.rate_lectur(lecturer_1, 'Python', 11)
student_2.rate_lectur(lecturer_2, 'Java', 10)

student_3.rate_lectur(lecturer_1, 'Python', 10)
student_3.rate_lectur(lecturer_2, 'Java', 8)
student_3.rate_lectur(lecturer_1, 'Python', 10)
student_3.rate_lectur(lecturer_2, 'Java', 9)
# пройденные курсы студентов ---------------------------------------
student_1.finished_courses += ['Основы Python', 'Разработка на Java']
student_2.finished_courses += ['Основы Python', 'Создание телеграмм ботов']
student_3.finished_courses += ['Основы Python', 'Тестировщик на Python']
# -------------------------------------------------------------------------
print(student_1, '\n')
print(student_2, '\n')
print(student_3, '\n')

print(lecturer_1, '\n')
print(lecturer_2, '\n')

print(reviewer_1, '\n')
print(reviewer_2, '\n')
# --------------------------------------------------------------------------
# сравниваем лекторов и студентов --------------------------------------------
print(lecturer_1 > student_1)
print(lecturer_2 < student_3)
print(lecturer_1 == student_2)
print(lecturer_2 != student_2)
# средняя оценка за ДЗ студентов по курсу -------------------------------------
students = [student_1, student_2, student_3]
def overall_rating_students(students, course):
  grades = 0
  for student in students:
      grade_course = student.grades.get(course)
      grades += sum(grade_course) / len(grade_course)
  return grades / len(students)
print()
print(f"Средняя оценка за ДЗ по всем студентам по курсу  Python: "
    f"{round(overall_rating_students(students, 'Python'), 2)}")
print(f"Средняя оценка за ДЗ по всем студентам по курсу Java: "
    f"{round(overall_rating_students(students, 'Java'), 2)}")
# средняя оценка лекторам -------------------------------------------------

lectors = [lecturer_1, lecturer_2]
def overall_rating_lectors(lectors, course):
  grades = 0
  for lector in lectors:
      grade_course = lector.grades.get(course)
      if grade_course is not None:
          grades += sum(grade_course) / len(grade_course)
  return grades
print(f"Средняя оценка лекторам по курсу  Python: "
    f"{round(overall_rating_lectors(lectors, 'Python'), 2)}")
print(f"Средняя оценка лекторам по курсу Java: "
    f"{round(overall_rating_lectors(lectors, 'Java'), 2)}")

