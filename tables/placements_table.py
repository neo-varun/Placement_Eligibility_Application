import mysql.connector
from faker import Faker
import random

fake=Faker()

class Placements:
        
    def __init__(self,num):

        self.num=num

        self.connection=mysql.connector.connect(
            host='localhost',
            user='root',
            password='2003',
            database='studentplacements'
        )

        self.cursor=self.connection.cursor()
        self.generate_fake_placements()

    def generate_fake_placements(self):

        self.cursor.execute("select student_id from students")
        student_ids = [row[0] for row in self.cursor.fetchall()]

        query='truncate table placements'
        self.cursor.execute(query)

        for i in range(min(self.num+1,len(student_ids))):
            
            placement_id=301+i
            student_id=student_ids[i]
            mock_interview_score=random.randint(1,100)
            internships_completed=random.randint(1,5)
            placement_status=random.choice(['Ready','Not Ready','Placed'])
            if placement_status=='Placed':
                company_name=fake.company()
                placement_package=random.randint(1,1600000)
                interview_rounds_cleared=random.randint(1,5)
                placement_date=fake.date_between(start_date="-2M", end_date="today")
            else:
                company_name=None
                placement_package=None
                interview_rounds_cleared=None
                placement_date=None
        
            query='insert into placements values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            values=(placement_id,student_id,mock_interview_score,internships_completed,placement_status,company_name,placement_package,interview_rounds_cleared,placement_date)
            self.cursor.execute(query,values)

            self.connection.commit()

        self.cursor.close()
        self.connection.close()