import mysql.connector
from tables.students_table import Students
from tables.programming_table import Programming
from tables.soft_skills_table import SoftSkills
from tables.placements_table import Placements

class DatabaseCreation:

    def __init__(self,num):

        self.num=num

        self.connection=mysql.connector.connect(
        host='localhost',
        user='root',
        password='2003',
        )
        
        self.cursor=self.connection.cursor()
        self.create_database_tables()

    def create_database_tables(self):
        
        query='create database if not exists studentplacements'
        self.cursor.execute(query)

        query='use studentplacements'
        self.cursor.execute(query)

        query='''create table if not exists students(
                student_id int primary key,
                name varchar(100) not null,
                age int check(age>=18),
                gender varchar(100) not null,
                email varchar(100) not null,
                phone varchar(100) not null,
                enrollment_year int check(enrollment_year>=2015),
                course_batch varchar(100) not null,
                city varchar(100) not null,
                graduation_year int not null)
            '''
        self.cursor.execute(query)

        query='''create table if not exists programming(
                programming_id int primary key,
                student_id int,
                language varchar(100) not null,
                problems_solved int not null,
                assessments_completed int not null,
                mini_projects int not null,
                certificates_earned int not null,
                latest_project_score int check(latest_project_score<=100),
                foreign key(student_id) references students(student_id))
            '''
        self.cursor.execute(query)

        query='''create table if not exists softskills(
                soft_skill_id int primary key,
                student_id int,
                communication int check(communication<=100),
                teamwork int check(teamwork<=100),
                presentation int check(presentation<=100),
                leadership int check(leadership<=100),
                critical_thinking int check(critical_thinking<=100),
                interpersonal_skills int check(interpersonal_skills<=100),
                foreign key(student_id) references students(student_id))
            '''
        self.cursor.execute(query)

        query='''create table if not exists placements(
                placement_id int primary key,
                student_id int,
                mock_interview_score int check(mock_interview_score<=100),
                internships_completed int not null,
                placement_status varchar(100) not null,
                company_name varchar(100),
                placement_package int,
                interview_rounds_cleared int,
                placement_date date)
            '''
        self.cursor.execute(query)

        Students(self.num)
        Programming(self.num)
        SoftSkills(self.num)
        Placements(self.num)

        self.connection.commit()
        self.cursor.close()
        self.connection.close()