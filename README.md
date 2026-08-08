# 🎓 Student Performance Analysis

### Interactive Student Data Analysis & Visualization Project

A complete **Student Performance Analysis** project that explores student academic performance using data cleaning, feature engineering, exploratory data analysis, statistical analysis, and interactive visualizations.

The project analyzes student scores, identifies relationships between different subjects, compares performance across groups, and generates useful insights from the dataset.

---

# 📖 Overview

Student Performance Analysis is a data analysis project developed using **Python**, **Pandas**, **NumPy**, **Matplotlib**, **Seaborn**, **Plotly**, and statistical analysis techniques.

The project uses a student performance dataset containing information about:

- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch
- Test Preparation Course
- Math Score
- Reading Score
- Writing Score

The main objective is to understand student performance patterns and discover meaningful relationships within the data.

---

# ✨ Features

### 📊 Data Analysis

- Dataset exploration
- Statistical summaries
- Score analysis
- Subject comparison
- Gender-based analysis
- Performance analysis

### 🧹 Data Cleaning

- Remove duplicate records
- Handle missing values
- Standardize column names
- Remove unnecessary spaces
- Prepare data for analysis

### ⚙️ Feature Engineering

- Calculate total score
- Calculate average score
- Create performance levels
- Generate additional useful features

### 📈 Data Visualization

- Score distribution
- Gender distribution
- Subject comparison
- Scatter plots
- Box plots
- Correlation heatmap
- Performance-level visualization

### 💡 Insights

The project identifies important patterns and relationships in student performance data.

---

# 🖥️ Project Dashboard

The project includes an interactive dashboard for exploring the student performance dataset.

![Student Performance Dashboard](images/dashboard.png)

---

# 📊 Visualizations

The project contains several visualizations generated during the analysis.

### 📈 Score Distribution

Shows the distribution of student scores and helps identify the overall performance pattern.

### 👥 Gender Distribution

Shows the number of students in each gender category.

### 📚 Subject Comparison

Compares student performance across:

- Mathematics
- Reading
- Writing

### 🔥 Correlation Heatmap

Shows relationships between numerical variables and identifies strongly correlated features.

### 📊 Performance Levels

Students are grouped according to their overall academic performance.

---

# 📂 Project Structure

```text
Student_Performance_Analysis/
│
├── 📁 data/
│   └── StudentsPerformance.csv
│
├── 📁 images/
│   ├── dashboard.png
│   ├── average_score_distribution.png
│   ├── correlation_heatmap.png
│   ├── gender_distribution.png
│   ├── performance_levels.png
│   └── subject_comparison.png
│
├── 📁 notebooks/
│   └── analysis.ipynb
│
├── 📁 reports/
│
├── 📁 src/
│   ├── app.py
│   ├── clean_data.py
│   ├── feature_engineering.py
│   ├── load_data.py
│   └── visualization.py
│
├── requirements.txt
│
└── README.md

🔄 Data Analysis Workflow
Raw Dataset
     │
     ▼
Data Loading
     │
     ▼
Data Cleaning
     │
     ▼
Feature Engineering
     │
     ▼
Exploratory Data Analysis
     │
     ▼
Data Visualization
     │
     ▼
Statistical Analysis
     │
     ▼
Insights & Findings
     │
     ▼
Interactive Dashboard

🛠️ Technologies Used
Technology	Purpose
Python	Programming
Pandas	Data Manipulation
NumPy	Numerical Computing
Matplotlib	Visualization
Seaborn	Statistical Visualization
Plotly	Interactive Visualization
Statsmodels	Statistical Analysis
Jupyter Notebook	Data Analysis
VS Code	Development
📊 Dataset

The project uses the Students Performance Dataset.

The dataset contains:

Feature	Description
Gender	Student gender
Race/Ethnicity	Student group
Parental Education	Parent's education level
Lunch	Lunch program type
Test Preparation	Test preparation status
Math Score	Mathematics score
Reading Score	Reading score
Writing Score	Writing score
Dataset Size
Original Records: 1000
Features: 8

After removing duplicate records:

Records: 999
🧹 Data Cleaning

The dataset was cleaned before performing analysis.

The cleaning process includes:

1. Remove Duplicates
df = df.drop_duplicates()
2. Standardize Column Names

For example:

math score

becomes:

math_score
3. Remove Extra Spaces

Text values are cleaned to ensure consistency.

4. Handle Missing Values

Missing records are removed before analysis.

⚙️ Feature Engineering

New features were created to make the analysis more meaningful.

Total Score

Combines:

Math Score
+
Reading Score
+
Writing Score
Average Score

Calculates the student's overall average performance.

Performance Level

Students are categorized according to their overall scores.

🔍 Exploratory Data Analysis

The analysis explores questions such as:

What is the average student score?
Which subject has the highest average score?
How does performance differ by gender?
How strongly are reading and writing scores related?
Which students are high performers?
How are scores distributed?
Which variables have strong correlations?
💡 Key Insights

The analysis provides insights such as:

📚 Reading and writing scores have a strong positive relationship.
📊 Student scores are concentrated around the middle-to-high score range.
👩‍🎓 Performance varies slightly between different student groups.
🏆 Students with consistently high scores across subjects are high performers.
🔗 Academic subjects show strong relationships with each other.
🎯 Learning Objectives

Through this project, I learned:

Working with real-world datasets
Loading CSV files
Data cleaning
Data preprocessing
Handling duplicates
Handling missing values
Feature engineering
Exploratory Data Analysis
Statistical analysis
Data visualization
Correlation analysis
Interactive dashboards
Python project organization
Writing reusable Python modules
📚 Skills Demonstrated
Python
Functions
Modules
File handling
Virtual environments
Project organization
Pandas
read_csv()
head()
tail()
shape
columns
dtypes
isnull()
dropna()
drop_duplicates()
value_counts()
groupby()
DataFrame filtering
Visualization
Histograms
Bar charts
Scatter plots
Box plots
Heatmaps
Interactive charts
🏗️ Project Architecture

The project is divided into multiple modules for better organization.

load_data.py
      │
      ▼
clean_data.py
      │
      ▼
feature_engineering.py
      │
      ▼
visualization.py
      │
      ▼
app.py
      │
      ▼
Interactive Dashboard

This modular structure makes the project easier to maintain and extend.

🚀 Future Improvements

Future versions of this project can include:

🤖 Machine Learning prediction
📈 Student score prediction
🎯 Grade prediction
🧠 High-performance classification
🌳 Random Forest model
📊 More advanced visualizations
🔍 Advanced statistical analysis
🤖 AI-generated insights
📱 Improved responsive interface
🤝 Contributing

Contributions, suggestions, and improvements are welcome.

To contribute:

Fork the repository
Create a new branch
Make your changes
Commit your changes
Push your changes
Open a Pull Request
👨‍💻 Author
Muhammad Faizan Aslam

Software Engineering Student

💻 Python Developer
📊 Data Science & Machine Learning Learner
🤖 AI Enthusiast
👁️ Computer Vision Learner

⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the repository

💡 Share your feedback

📄 License

This project is licensed under the MIT License.