from random import randint



class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_in_progress = []
        self.finished_courses = []
        self.grades = {}
        self.average_grade = []

    @classmethod
    def verify_average(cls, other):
        if not isinstance(other, (int, Student)):
            raise TypeError(f'Значение должно быть целым числом и принадлежать классу {cls.__init__}')

        return other if isinstance(other, int) else other.average_grade


    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade}\n" \
               f"Курсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}"


    def add_courses(self, course):
        self.courses_in_progress.append(course)
        self.finished_courses.append(course)


    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            raise Exception('Ошибка')

    def get_average_grade(self):
        grades_list = []
        for course in self.grades:
            for grade in self.grades[course]:
                grades_list += [grade]
                self.average_grade = sum(grades_list) / len(grades_list)
            return f"Средняя оценка за домашние задания: {self.average_grade}"

    def __eq__(self, other):
        return self.average_grade == self.verify_average(other)


    def __lt__(self, other):
        return self.average_grade < self.verify_average(other)



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grade = []

    @classmethod
    def verify_average(cls, other):
        if not isinstance(other, (int, Lecturer)):
            raise TypeError('Значение должно быть целым числом и принадлежать классу Lecturer')

        return other if isinstance(other, int) else other.average_grade


    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade}"


    def get_average_grade(self):
        grades_list = []
        for course in self.grades:
            for grade in self.grades[course]:
                grades_list += [grade]
                self.average_grade = sum(grades_list) / len(grades_list)
            return f"Средняя оценка за лекции: {self.average_grade}"


    def __eq__(self, other):
        return self.average_grade == self.verify_average(other)



    def __lt__(self, other):
        return self.average_grade < self.verify_average(other)


class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            raise Exception('Ошибка')



student1 = Student('Tom', 'Soyer')
student1.courses_in_progress += ['Python', 'Django']
student1.finished_courses += ['SQL', 'Java']

student2 = Student('Gek', 'Finn')
student2.courses_in_progress += ['Django', 'SQL', 'Java']
student2.finished_courses += ['Python']

lecturer1 = Lecturer('John', 'Lock')
lecturer1.courses_attached += ['Python', 'Django']

lecturer2 = Lecturer('Donald', 'Tramp')
lecturer2.courses_attached += ['Java', 'SQL']

reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += ['Python', 'SQL']

reviewer2 = Reviewer('Tom', 'Redl')
reviewer2.courses_attached += ['Django', 'Java']

print('============================')
print(reviewer1)
print(reviewer1.__dict__)
print()
print(reviewer2)
print(reviewer2.__dict__)

print('============================')
reviewer1.rate_student(student1, 'Python', 8)
reviewer1.rate_student(student1, 'Python', 9)
reviewer2.rate_student(student1, 'Django', 8)
reviewer2.rate_student(student1, 'Django', 9)
print(student1.grades)
print(student1.get_average_grade())
print(student1.__dict__)
print(student1)
print()

reviewer1.rate_student(student2, 'SQL', 10)
reviewer1.rate_student(student2, 'SQL', 9)
reviewer2.rate_student(student2, 'Django', 9)
reviewer2.rate_student(student2, 'Java', 9)
print(student2.grades)
print(student2.get_average_grade())
print(student2.__dict__)
print(student2)
print('-----------')
print(student1 == student2)
print(student1 < student2)



print('============================')

student1.rate_lecturer(lecturer1, 'Python', 8)
student1.rate_lecturer(lecturer1, 'Django', 8)
student2.rate_lecturer(lecturer1, 'Django', 9)
student2.rate_lecturer(lecturer1, 'Django', 10)
print(lecturer1.grades)
print(lecturer1.get_average_grade())
print(lecturer1.__dict__)
print(lecturer1)
print()

student2.rate_lecturer(lecturer2, 'SQL', 10)
student2.rate_lecturer(lecturer2, 'Java', 9)
print(lecturer2.grades)
print(lecturer2.get_average_grade())
print(lecturer2.__dict__)
print(lecturer2)

print(lecturer1 == lecturer2)
print(lecturer1 < lecturer2)



student = []

courses_in_progress = [
    {'name': 'Tom', 'surname': 'Soyer', 'course': ['Python', 'Django']},
    {'name': 'Gek', 'surname': 'Finn',  'course': ['Django', 'SQL', 'Java']}]


courses_attached = [
    {'name': 'John', 'surname': 'Lock', 'course': ['Python', 'Django']},
    {'name': 'Donald', 'surname': 'Tramp',  'course': ['Django', 'SQL']}

]

for item in courses_in_progress:
    student, course, grade = item.values()
    student.append(Reviewer(student, course))

for i in courses_attached:
    i.add_courses(i.student.grades, randint(1, 10))

for i in courses_attached:
    print(i.student.courses_in_progress)

def calc(student_list: list):
    if not student_list:
        return 0

    grades_list = []
    for i in student_list:
        grades_list += i.grade

    result = sum(grades_list) / len(grades_list)
    return result

print(calc(student))





