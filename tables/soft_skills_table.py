import mysql.connector
import random

class SoftSkills:

    def __init__(self,num):

        self.num=num

        self.connection=mysql.connector.connect(
            host='localhost',
            user='root',
            password='2003',
            database='studentplacements'
        )

        self.cursor=self.connection.cursor()
        self.generate_fake_softskills()

    def generate_fake_softskills(self):

        self.cursor.execute("select student_id from students")
        student_ids = [row[0] for row in self.cursor.fetchall()]

        query='truncate table softskills'
        self.cursor.execute(query)

        for i in range(min(self.num+1,len(student_ids))):

            soft_skill_id=201+i
            student_id=student_ids[i]
            communication=random.randint(1,100)
            teamwork=random.randint(1,100)
            presentation=random.randint(1,100)
            leadership=random.randint(1,100)
            critical_thinking=random.randint(1,100)
            interpersonal_skills=random.randint(1,100)

            query='insert into softskills values(%s,%s,%s,%s,%s,%s,%s,%s)'
            values=(soft_skill_id,student_id,communication,teamwork,presentation,leadership,critical_thinking,interpersonal_skills)
            self.cursor.execute(query,values)

            self.connection.commit()

        self.cursor.close()
        self.connection.close()