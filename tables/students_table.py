import mysql.connector
from faker import Faker
import random

fake=Faker()

class Students:

    def __init__(self,num):
        
        self.num=num

        self.connection=mysql.connector.connect(
            host='localhost',
            user='root',
            password='2003',
            database='studentplacements'
        )

        self.cursor=self.connection.cursor()
        self.generate_fake_students()

    def generate_fake_students(self):

        self.cursor.execute('set foreign_key_checks = 0')
        self.cursor.execute('delete from students')
        self.cursor.execute('set foreign_key_checks = 1')
        
        for i in range(1,self.num+1):

            student_id=i
            name=fake.name()
            age=random.randint(18,100)
            gender=random.choice(['Male','Female','Other'])
            email=fake.email()
            phone=fake.phone_number()
            enrollment_year=random.randint(2015,2025)
            course_batch=random.choice(['AI/ML','Data Science','Full Stack Development','DevOps','Selenium Automation','UI/UX','Java Automation'])
            city=fake.city()
            graduation_year = enrollment_year + random.choice([3, 4, 5])

            query='insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            values=(student_id,name,age,gender,email,phone,enrollment_year,course_batch,city,graduation_year)
            self.cursor.execute(query,values)

            self.connection.commit()

        self.cursor.close()
        self.connection.close()