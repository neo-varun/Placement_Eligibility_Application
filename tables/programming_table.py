import mysql.connector
import random

class Programming:

    def __init__(self,num):
        
        self.num=num

        self.connection=mysql.connector.connect(
            host='localhost',
            user='root',
            password='2003',
            database='studentplacements'
        )
        
        self.cursor=self.connection.cursor()
        self.generate_fake_programming()

    def generate_fake_programming(self):

        self.cursor.execute("select student_id from students")
        student_ids = [row[0] for row in self.cursor.fetchall()]
        
        query='truncate table programming'
        self.cursor.execute(query)

        for i in range(min(self.num+1,len(student_ids))):

            programming_id=101+i
            student_id=student_ids[i]
            language=random.choice(['Python','C','C++','Ruby','JavaScript','Java'])
            problems_solved=random.randint(1,1000)
            assessments_completed=random.randint(1,30)
            mini_projects=random.randint(1,10)
            certificates_earned=random.randint(1,200)
            latest_project_score=random.randint(1,100)

            query='insert into programming values(%s,%s,%s,%s,%s,%s,%s,%s)'
            values=(programming_id,student_id,language,problems_solved,assessments_completed,mini_projects,certificates_earned,latest_project_score)
            self.cursor.execute(query,values)

            self.connection.commit()

        self.cursor.close()
        self.connection.close()