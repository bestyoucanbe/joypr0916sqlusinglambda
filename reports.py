import sqlite3


class Student():

    def __init__(self, first, last, handle, cohort):
        self.first_name = first
        self.last_name = last
        self.slack_handle = handle
        self.cohort = cohort


class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/Owner/workspace/practices/joypr0912sqlcreatestudentdb/studentexercises.db"

    # Using lambda (anonymous Python function) to create the results--don't need create_student anymore...
    # def create_student(self, cursor, row):
    #     return Student(row[1], row[2], row[3], row[5])

    def all_students(self):
        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:

            conn.row_factory = lambda cursor, row: Student(
                row[1], row[2], row[3], row[5])

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.Id,
                s.First_Name,
                s.Last_Name,
                s.Slack_Handle,
                s.Cohort_Id,
                c.Name
            from Student s
            join Cohort c on s.Cohort_Id = c.Id
            order by s.Cohort_Id
            """)

            all_students = db_cursor.fetchall()

            # for student in all_students:
            #     print(f'{student[1]} {student[2]} is in {student[5]}')

            for student in all_students:
                print(
                    f'{student.first_name} {student.last_name} is in {student.cohort}')


reports = StudentExerciseReports()
reports.all_students()
