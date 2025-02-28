import os
import sys
import pandas as pd
import streamlit as st
import mysql.connector

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database_table import DatabaseCreation

connection=mysql.connector.connect(
    host='localhost',
    user='root',
    password='2003',
)

cursor=connection.cursor()

st.set_page_config(page_title="Placement Eligibility App", layout="wide")

st.title("Placement Eligibility App")

st.header('Welcome! Click the button below to create the necessary database tables')

if st.button('Create Tables'):
    
    DatabaseCreation(750)

table=st.selectbox(label='Select the table you want to view',options=['Students','Programming','Soft Skills','Placements'])

if st.button('View Table'):

    cursor.execute('use studentplacements')

    if table=='Students':

        cursor.execute('select * from students')

    elif table=='Programming':

        cursor.execute('select * from programming')

    elif table=='Soft Skills':

        cursor.execute('select * from softskills')

    elif table=='Placements':

        cursor.execute('select * from placements')

    column_names = [i[0] for i in cursor.description]
    data=cursor.fetchall()

    df=pd.DataFrame(data,columns=column_names)

    st.dataframe(df)

st.header("Placement Eligibility Criteria")

st.write('To be eligible for placements, a student must meet the following requirements:')
st.write('- Solve at least **300** problems in their programming language')
st.write('- Complete a minimum of **12** assessments')
st.write('- Achieve a communication skills score greater than **50**')
st.write('- Attain an interpersonal skills score greater than **50**')
st.write('- Obtain a mock interview score of at least **30**')

st.header('View Eligible Students')

create_eligible_table=st.button('View Eligible Students')

if create_eligible_table:

    cursor.execute('use studentplacements')

    query = ''' select * from students
            where student_id in(
            select student_id from programming
            where problems_solved>=300 and assessments_completed>=12)
            and student_id in(
            select student_id from softskills
            where communication>=50 and interpersonal_skills>=50)
            and student_id in(
            select student_id from placements
            where mock_interview_score>=30)
    '''
    cursor.execute(query)

    column_names = [i[0] for i in cursor.description]
    data=cursor.fetchall()

    df=pd.DataFrame(data,columns=column_names)

    st.dataframe(df)