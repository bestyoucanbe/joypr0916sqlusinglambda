import sqlite3


class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/Owner/workspace/practices/joypr0912sqlcreatestudentdb/studentexercises.db"

    def all_students(self):
        """Retrieve all students with the cohort name"""

        with sqlite3.connect("/Users/Owner/workspace/practices/joypr0912sqlcreatestudentdb/studentexercises.db") as conn:
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

            for student in all_students:
                print(f'{student[1]} {student[2]} is in {student[5]}')


reports = StudentExerciseReports()
reports.all_students()
