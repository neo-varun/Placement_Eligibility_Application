import pandas as pd
import streamlit as st
import mysql.connector
import matplotlib.pyplot as plt

connection=mysql.connector.connect(
    host='localhost',
    user='root',
    password='2003',
)

cursor=connection.cursor()

cursor.execute("show databases")
databases = [db[0] for db in cursor.fetchall()]

if "studentplacements" not in databases:
    st.write("Database not found. Please create it on the first page.")

else:

    st.title('Student Placement Analytics')

    st.header('Explore 10 Different Insights into the Data')

    table=st.selectbox(label='Select the insight you want to view',options=[
                        'Students enrolled in AI/ML in the last 5 years',
                        'Students with teamwork and leadership scores above 60',
                        'Students placed in the last week with a package above 8 LPA',
                        'Full Stack Development students who completed more than 10 assessments',
                        'Students with a mock interview score above 50, completed more than 1 internship, and are not placed',
                        'Programming languages vs. average number of problems solved - Bar plot',
                        "Programming language vs. students' critical thinking skills - Bar plot",
                        'Placed students by course - Pie plot',
                        'Salary distribution of placed students - Pie plot',
                        'Mock interview scores vs. placement packages - Scatter plot',])

    if st.button("View Insights"):

        cursor.execute('use studentplacements')

        if table == "Students enrolled in AI/ML in the last 5 years": #1

            st.write("This insight lists students enrolled in the AI/ML course within the last five years.")
            cursor.execute('select * from students where course_batch="AI/ML" and enrollment_year>=2019')
            column_names = [i[0] for i in cursor.description]
            data=cursor.fetchall()
            df=pd.DataFrame(data,columns=column_names)
            st.dataframe(df)

        elif table == "Students with teamwork and leadership scores above 60": #2

            st.write("This insight displays students who have demonstrated strong teamwork and leadership skills, scoring above 60 in both areas.")
            cursor.execute('''select * from students where student_id in(
                        select student_id from softskills where teamwork>=60 and leadership>=60)''')
            column_names = [i[0] for i in cursor.description]
            data=cursor.fetchall()
            df=pd.DataFrame(data,columns=column_names)
            st.dataframe(df)

        elif table == "Students placed in the last week with a package above 8 LPA": #3

            st.write("This insight identifies students placed in the last week with a salary package exceeding 8 LPA, highlighting recent high-value placements.")
            cursor.execute('''select * from students where student_id in(
                        select student_id from placements where placement_date is not null
                        and placement_date>=date_sub(curdate(), interval 7 day) and placement_package>=800000)''')
            column_names = [i[0] for i in cursor.description]
            data=cursor.fetchall()
            df=pd.DataFrame(data,columns=column_names)
            st.dataframe(df)

        elif table == "Full Stack Development students who completed more than 10 assessments": #4 - Cross table

            st.write("This insight lists students from the Full Stack Development course who have completed more than 10 assessments, highlighting their commitment.")
            cursor.execute('''select * from students where course_batch="Full Stack Development" and student_id in(
                        select student_id from programming where assessments_completed>=10)''')
            column_names = [i[0] for i in cursor.description]
            data=cursor.fetchall()
            df=pd.DataFrame(data,columns=column_names)
            st.dataframe(df)

        elif table == "Students with a mock interview score above 50, completed more than 1 internship, and are not placed": #5
            
            st.write("This insight lists students who have performed well in mock interviews and internships but have not yet secured placements, identifying potential candidates for further support.")
            cursor.execute('''select * from students where student_id in(
                        select student_id from placements where mock_interview_score>=50 and internships_completed>=1 and placement_status="Ready")''')
            column_names = [i[0] for i in cursor.description]
            data=cursor.fetchall()
            df=pd.DataFrame(data,columns=column_names)
            st.dataframe(df)
        
        elif table == "Programming languages vs. average number of problems solved - Bar plot": #6 - Bar plot

            st.write("This insight visualizes the average number of problems solved by students for each programming language, helping identify proficiency trends.")  # Bar plot
            cursor.execute('select language,avg(problems_solved) from programming group by language')
            data=cursor.fetchall()
            df=pd.DataFrame(data,columns=['Programming Language','Avg Problems Solved'])
            fig, ax = plt.subplots(figsize=(10,5))
            ax.bar(df["Programming Language"], df["Avg Problems Solved"], color="royalblue")
            ax.set_xlabel("Programming Language", fontsize=8)
            ax.set_ylabel("Avg Problems Solved", fontsize=8)
            ax.set_title("Programming Languages vs. Avg Problems Solved", fontsize=10)
            plt.xticks(rotation=30, ha="right", fontsize=7)
            plt.tight_layout()
            st.pyplot(fig)

        elif table == "Programming language vs. students' critical thinking skills - Bar plot": #7 - Bar plot

            st.write("This insight visualizes the average critical thinking scores of students across various programming languages.")
            cursor.execute('select p.language, avg(s.critical_thinking) from programming p join softskills s on p.student_id = s.student_id group by p.language')
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=["Programming Language", "Avg Critical Thinking"])
            fig, ax = plt.subplots(figsize=(10,5))
            ax.bar(df["Programming Language"], df["Avg Critical Thinking"], color="royalblue")
            ax.set_xlabel("Programming Language", fontsize=8)
            ax.set_ylabel("Avg Critical Thinking", fontsize=8)
            ax.set_title("Programming Language vs. Avg Critical Thinking", fontsize=10)
            plt.xticks(rotation=30, ha="right", fontsize=7)
            plt.tight_layout()
            st.pyplot(fig)

        elif table == "Placed students by course - Pie plot": #8 - Pie plot

            st.write("This insight presents a distribution of placed students based on their respective courses, giving an overview of placement trends.")
            query = 'select s.course_batch, count(*) from students s join placements p on s.student_id = p.student_id where p.placement_status = "placed" group by s.course_batch'
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=["Course", "Placed Students"])
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.pie(df["Placed Students"], labels=df["Course"], autopct="%1.1f%%", colors=plt.cm.Paired.colors,textprops={'fontsize':7})
            ax.set_title("Placed Students by Course", fontsize=10)
            st.pyplot(fig)

        elif table == "Salary distribution of placed students - Pie plot": #9 - Pie plot

            st.write("This insight provides an overview of salary distribution among placed students, highlighting trends in compensation packages.")
            cursor.execute("""
            select 
                case 
                    when placement_package < 400000 then 'Below 4 LPA'
                    when placement_package between 400000 and 600000 then '4-6 LPA'
                    when placement_package between 600000 and 1000000 then '6-10 LPA'
                    when placement_package > 1000000 then 'Above 10 LPA'
                end as salary_range,
                count(*) 
            from placements
            where placement_status = 'Placed' and placement_package is not null
            group by salary_range
            """)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=["Salary Range", "Count"])
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.pie(df["Count"], labels=df["Salary Range"], autopct="%1.1f%%", colors=plt.cm.Paired.colors,textprops={'fontsize':7})
            ax.set_title("Salary Distribution of Placed Students", fontsize=10)
            st.pyplot(fig)

        elif table == "Mock interview scores vs. placement packages - Scatter plot": #10 - Scatter plot

            st.write("This insight explores the relationship between students' mock interview scores and their placement packages.")
            cursor.execute('select mock_interview_score, placement_package from placements where placement_status = "Placed" and placement_package is not null')
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=["Mock Interview Score", "Placement Package"])
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.scatter(df["Mock Interview Score"], df["Placement Package"], color="royalblue", alpha=0.7)
            ax.set_xlabel("Mock Interview Score", fontsize=10)
            ax.set_ylabel("Placement Package (in LPA)", fontsize=10)
            ax.set_title("Mock Interview Score vs. Placement Package", fontsize=10)
            plt.tight_layout()
            st.pyplot(fig)