# Student Placement Eligibility & Analytics App

## Overview
This project is a **Student Placement Eligibility & Analytics App** built using **Streamlit** and **MySQL**. It allows institutions to **track, analyze, and visualize student placement readiness** based on **programming skills, soft skills, and placement records**.

The application automatically **creates a database and tables**, generates **sample data**, and provides **interactive dashboards** for eligibility checking and analytics.

## Features
- **Automatic Database & Table Creation** – The app initializes MySQL and populates sample data
- **Placement Eligibility Criteria Check** – Identify students who qualify for placements
- **Data Visualization & Insights** – Bar charts, pie charts, and scatter plots for analysis
- **Multi-Page Navigation** – Separate pages for criteria validation and data analytics

## Prerequisites

### Install MySQL
Before running the application, you must have **MySQL** installed and running on your system.

- **Windows:** Download and install MySQL from [MySQL Official Site](https://dev.mysql.com/downloads/installer/)
- **Linux:**  
  ```bash
  sudo apt install mysql-server
  ```
- **macOS:**  
  ```bash
  brew install mysql
  ```  
- After installation, start the MySQL server and set up a **root user** with a password.

## Installation & Setup

### Create a Virtual Environment (Recommended)
It is recommended to create a virtual environment to manage dependencies:
```bash
python -m venv venv
```
Activate the virtual environment:
- **Windows:**  
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux:**  
  ```bash
  source venv/bin/activate
  ```

### Install Dependencies
Ensure you have **Python 3.x** installed, then install the required packages:
```bash
pip install -r requirements.txt
```

### Run the Streamlit App
Navigate to the **streamlit** folder:
```bash
cd streamlit
```
Then run the **Criteria_Page.py** file:
```bash
streamlit run Criteria_Page.py
```

## How the Program Works

### Application Initialization
- When the application is launched, it **connects to MySQL** and checks if the **database exists**.
- If not found, the app **creates the `studentplacements` database and tables**.
- It **populates tables with sample data** using the `Faker` library.

### Placement Eligibility Criteria (Criteria_Page.py)
- Displays the **minimum requirements** for students to be **eligible for placements**.
- Clicking **"View Eligible Students"** filters students based on:
  - 300+ programming problems solved
  - 12+ assessments completed
  - Communication skills score > 50
  - Interpersonal skills score > 50
  - Mock interview score ≥ 30
- The results are displayed in a **table** within the app.

### Data Insights & Visualizations (Query_Page.py)
- Users can select from **10 different insights**, including:
  - Students enrolled in AI/ML in the last 5 years
  - Students with teamwork and leadership scores above 60
  - Recently placed students with packages above 8 LPA
  - Mock interview scores vs. placement packages (scatter plot)
  - Salary distribution of placed students (pie chart)
  - Programming languages vs. average problems solved (bar chart)
- The app **queries MySQL**, retrieves results, and **renders data as tables or charts** using **Matplotlib** and **Pandas**.

## Usage Guide

### Create Tables & Populate Data
- On the **Criteria Page**, click **"Create Tables"** to automatically generate the database and tables.

### View Student Data
- Select a table (`Students`, `Programming`, `Soft Skills`, `Placements`) and click **"View Table"** to see records.

### Check Placement Eligibility
- Click **"View Eligible Students"** to see which students qualify for placements based on predefined criteria.

### Explore Insights & Analytics
- Go to the **Query Page** to analyze **placement trends, salary distributions, and programming proficiency** using **interactive charts**.

## Technologies Used
- **Python**
- **Streamlit** (Frontend & UI)
- **MySQL** (Database)
- **Matplotlib & Pandas** (Data Visualization)
- **Faker & Random** (Data Generation)

## License
This project is licensed under the **MIT License**.

## Author
Developed by **Varun**. Feel free to connect with me on:
- **Email:** darklususnaturae@gmail.com