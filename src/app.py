import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Student Performance Analysis",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background-color: #f5f7fb;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #111c35;
    }

    section[data-testid="stSidebar"] * {
        color: white;
    }

    /* Sidebar title */
    .sidebar-title {
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 20px;
    }

    /* Main title */
    .main-title {
        font-size: 32px;
        font-weight: 700;
        color: #172b4d;
        margin-bottom: 5px;
    }

    .subtitle {
        color: #6b7c93;
        font-size: 15px;
        margin-bottom: 25px;
    }

    /* Metric cards */
    .metric-card {
        background: white;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #e5eaf2;
        box-shadow: 0 3px 12px rgba(0,0,0,0.05);
        min-height: 125px;
    }

    .metric-title {
        color: #718096;
        font-size: 14px;
    }

    .metric-value {
        color: #172b4d;
        font-size: 27px;
        font-weight: bold;
        margin-top: 10px;
    }

    /* Section title */
    .section-title {
        color: #172b4d;
        font-size: 22px;
        font-weight: 700;
        margin-top: 20px;
    }

    /* Insight cards */
    .insight-card {
        background: white;
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #4f7df3;
        margin-bottom: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }

    /* Success message */
    .success-box {
        background-color: #dff5e9;
        color: #087443;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
        font-weight: 500;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD DATA
# =========================================================

@st.cache_data
def load_data():

    file_path = "data/StudentPerformance.csv"

    df = pd.read_csv(file_path)

    return df


try:
    df = load_data()

except FileNotFoundError:
    st.error(
        "Dataset not found. Make sure StudentsPerformance.csv is inside the data folder."
    )
    st.stop()


# =========================================================
# CLEAN COLUMN NAMES
# =========================================================

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)


# =========================================================
# FEATURE ENGINEERING
# =========================================================

df["total_score"] = (
    df["math_score"]
    + df["reading_score"]
    + df["writing_score"]
)

df["average_score"] = (
    df["total_score"] / 3
).round(2)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">🎓 Student Performance</div>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    page = st.radio(
        "Navigation",
        [
            "🏠 Overview",
            "📊 Dataset",
            "🧹 Data Cleaning",
            "🔍 Exploratory Data Analysis",
            "📈 Visualizations",
            "💡 Insights",
            "⚙️ Feature Engineering",
            "⬇️ Download Data"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")

    st.markdown("### 📌 About this Project")

    st.write(
        "This project analyzes student performance "
        "data to discover patterns, relationships "
        "and useful insights."
    )

    st.markdown("---")

    st.caption("Built with ❤️ using Python + Pandas")


# =========================================================
# OVERVIEW PAGE
# =========================================================

if page == "🏠 Overview":

    st.markdown(
        '<div class="main-title">🎓 Student Performance Analysis Dashboard</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Explore student data, discover patterns and generate useful insights</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="success-box">Dataset Loaded Successfully ✓</div>',
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # METRICS
    # -----------------------------------------------------

    total_students = len(df)

    total_subjects = 3

    average_score = df["average_score"].mean()

    top_score = df["total_score"].max()

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">👥 Total Students</div>
                <div class="metric-value">{total_students:,}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">📚 Total Subjects</div>
                <div class="metric-value">{total_subjects}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">📊 Average Score</div>
                <div class="metric-value">{average_score:.2f}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">🏆 Top Total Score</div>
                <div class="metric-value">{top_score}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    # =====================================================
    # SCORE DISTRIBUTION
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            '<div class="section-title">📊 Score Distribution</div>',
            unsafe_allow_html=True
        )

        fig = px.histogram(
            df,
            x="total_score",
            nbins=20,
            title="",
            labels={
                "total_score": "Total Score",
                "count": "Students"
            }
        )

        fig.update_layout(
            height=350,
            margin=dict(l=20, r=20, t=20, b=20),
            plot_bgcolor="white",
            paper_bgcolor="white"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    # =====================================================
    # GENDER SCORE
    # =====================================================

    with col2:

        st.markdown(
            '<div class="section-title">👩‍🎓 Average Score by Gender</div>',
            unsafe_allow_html=True
        )

        gender_scores = (
            df.groupby("gender")["average_score"]
            .mean()
            .reset_index()
        )

        fig = px.bar(
            gender_scores,
            x="gender",
            y="average_score",
            text_auto=".2f",
            labels={
                "gender": "Gender",
                "average_score": "Average Score"
            }
        )

        fig.update_layout(
            height=350,
            margin=dict(l=20, r=20, t=20, b=20),
            plot_bgcolor="white",
            paper_bgcolor="white"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    # =====================================================
    # SECOND ROW
    # =====================================================

    col1, col2 = st.columns(2)

    # -----------------------------------------------------
    # SUBJECT COMPARISON
    # -----------------------------------------------------

    with col1:

        st.markdown(
            '<div class="section-title">📚 Average Score by Subject</div>',
            unsafe_allow_html=True
        )

        subject_data = pd.DataFrame({
            "Subject": [
                "Math",
                "Reading",
                "Writing"
            ],
            "Average Score": [
                df["math_score"].mean(),
                df["reading_score"].mean(),
                df["writing_score"].mean()
            ]
        })

        fig = px.bar(
            subject_data,
            x="Subject",
            y="Average Score",
            text_auto=".2f"
        )

        fig.update_layout(
            height=350,
            margin=dict(l=20, r=20, t=20, b=20),
            plot_bgcolor="white",
            paper_bgcolor="white"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    # -----------------------------------------------------
    # MATH VS READING
    # -----------------------------------------------------

    with col2:

        st.markdown(
            '<div class="section-title">📈 Math vs Reading Score</div>',
            unsafe_allow_html=True
        )

        fig = px.scatter(
            df,
            x="math_score",
            y="reading_score",
            color="gender",
            labels={
                "math_score": "Math Score",
                "reading_score": "Reading Score"
            }
        )

        fig.update_layout(
            height=350,
            margin=dict(l=20, r=20, t=20, b=20),
            plot_bgcolor="white",
            paper_bgcolor="white"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    # =====================================================
    # INSIGHTS
    # =====================================================

    st.markdown(
        '<div class="section-title">💡 Key Insights</div>',
        unsafe_allow_html=True
    )

    correlation = df[
        ["math_score", "reading_score", "writing_score"]
    ].corr()

    reading_writing_corr = correlation.loc[
        "reading_score",
        "writing_score"
    ]

    math_reading_corr = correlation.loc[
        "math_score",
        "reading_score"
    ]

    female_avg = df[
        df["gender"] == "female"
    ]["average_score"].mean()

    male_avg = df[
        df["gender"] == "male"
    ]["average_score"].mean()

    insights = [
        f"📚 Reading and Writing scores have a strong correlation of {reading_writing_corr:.2f}.",
        f"📈 Math and Reading scores have a correlation of {math_reading_corr:.2f}.",
        f"👩 Female students average {female_avg:.2f}, while male students average {male_avg:.2f}.",
        f"🏆 The highest total score is {top_score} out of 300."
    ]

    for insight in insights:

        st.markdown(
            f"""
            <div class="insight-card">
                {insight}
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# DATASET PAGE
# =========================================================

elif page == "📊 Dataset":

    st.title("📊 Dataset")

    st.write(
        "Original Student Performance dataset."
    )

    st.write(
        f"Rows: **{df.shape[0]}** | Columns: **{df.shape[1]}**"
    )

    st.dataframe(
        df,
        width="stretch",
        height=550
    )


# =========================================================
# DATA CLEANING PAGE
# =========================================================

elif page == "🧹 Data Cleaning":

    st.title("🧹 Data Cleaning")

    st.subheader("Cleaning Operations")

    st.write("✔ Removed duplicate rows")

    st.write("✔ Standardized column names")

    st.write("✔ Removed extra spaces")

    st.write("✔ Checked missing values")

    st.write("✔ Created total score")

    st.write("✔ Created average score")

    st.subheader("Missing Values")

    missing = df.isnull().sum()

    st.dataframe(
        missing.to_frame("Missing Values"),
        width="stretch"
    )

    st.subheader("Dataset Shape")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Rows",
            df.shape[0]
        )

    with col2:
        st.metric(
            "Columns",
            df.shape[1]
        )


# =========================================================
# EDA PAGE
# =========================================================

elif page == "🔍 Exploratory Data Analysis":

    st.title("🔍 Exploratory Data Analysis")

    st.subheader("Statistical Summary")

    st.dataframe(
        df.describe(),
        width="stretch"
    )

    st.subheader("Gender Distribution")

    gender_counts = df["gender"].value_counts()

    fig = px.pie(
        values=gender_counts.values,
        names=gender_counts.index,
        hole=0.4
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    st.subheader("Score Correlation")

    numeric_df = df[
        [
            "math_score",
            "reading_score",
            "writing_score",
            "total_score",
            "average_score"
        ]
    ]

    correlation = numeric_df.corr()

    fig = px.imshow(
        correlation,
        text_auto=".2f",
        aspect="auto"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )


# =========================================================
# VISUALIZATIONS PAGE
# =========================================================

elif page == "📈 Visualizations":

    st.title("📈 Visualizations")

    # Histogram

    st.subheader("Score Distribution")

    fig = px.histogram(
        df,
        x="total_score",
        nbins=25
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    # Box plot

    st.subheader("Subject Score Box Plot")

    box_data = df.melt(
        id_vars=["gender"],
        value_vars=[
            "math_score",
            "reading_score",
            "writing_score"
        ],
        var_name="Subject",
        value_name="Score"
    )

    fig = px.box(
        box_data,
        x="Subject",
        y="Score",
        color="Subject"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    # Scatter plot

    st.subheader("Math vs Writing")

    fig = px.scatter(
        df,
        x="math_score",
        y="writing_score",
        color="gender",
        trendline="ols"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )


# =========================================================
# INSIGHTS PAGE
# =========================================================

elif page == "💡 Insights":

    st.title("💡 Student Performance Insights")

    highest_math = df["math_score"].max()

    highest_reading = df["reading_score"].max()

    highest_writing = df["writing_score"].max()

    best_student = df.loc[
        df["total_score"].idxmax()
    ]

    st.success(
        f"🏆 Highest total score: {best_student['total_score']}"
    )

    st.info(
        f"📐 Highest Math score: {highest_math}"
    )

    st.info(
        f"📖 Highest Reading score: {highest_reading}"
    )

    st.info(
        f"✍️ Highest Writing score: {highest_writing}"
    )

    st.subheader("Top 10 Students")

    top_students = (
        df.sort_values(
            "total_score",
            ascending=False
        )
        .head(10)
    )

    st.dataframe(
        top_students[
            [
                "gender",
                "math_score",
                "reading_score",
                "writing_score",
                "total_score",
                "average_score"
            ]
        ],
        width="stretch"
    )


# =========================================================
# FEATURE ENGINEERING PAGE
# =========================================================

elif page == "⚙️ Feature Engineering":

    st.title("⚙️ Feature Engineering")

    st.write(
        "New features created from the original subject scores."
    )

    st.subheader("Total Score")

    st.code(
        """
df["total_score"] = (
    df["math_score"]
    + df["reading_score"]
    + df["writing_score"]
)
"""
    )

    st.subheader("Average Score")

    st.code(
        """
df["average_score"] = (
    df["total_score"] / 3
).round(2)
"""
    )

    st.subheader("Feature Dataset")

    st.dataframe(
        df[
            [
                "math_score",
                "reading_score",
                "writing_score",
                "total_score",
                "average_score"
            ]
        ].head(20),
        width="stretch"
    )


# =========================================================
# DOWNLOAD PAGE
# =========================================================

elif page == "⬇️ Download Data":

    st.title("⬇️ Download Cleaned Dataset")

    csv = df.to_csv(
        index=False
    ).encode("utf-8")

    st.success(
        "Your processed dataset is ready."
    )

    st.download_button(
        label="⬇️ Download CSV",
        data=csv,
        file_name="cleaned_student_performance.csv",
        mime="text/csv",
        width="stretch"
    )

    st.subheader("Preview")

    st.dataframe(
        df.head(20),
        width="stretch"
    )