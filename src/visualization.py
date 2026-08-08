import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from clean_data import clean_data
from feature_engineering import add_features


def load_data():
    """Load, clean and feature-engineer the dataset."""

    file_path = "data/StudentPerformance.csv"

    df = pd.read_csv(file_path)

    df = clean_data(df)

    df = add_features(df)

    return df


def plot_gender_distribution(df):
    """Show number of male and female students."""

    plt.figure(figsize=(8, 5))

    sns.countplot(
        data=df,
        x="gender"
    )

    plt.title("Student Gender Distribution")
    plt.xlabel("Gender")
    plt.ylabel("Number of Students")

    plt.tight_layout()

    plt.savefig("images/gender_distribution.png")

    plt.show()


def plot_score_distribution(df):
    """Show distribution of average student scores."""

    plt.figure(figsize=(8, 5))

    sns.histplot(
        data=df,
        x="average_score",
        bins=20,
        kde=True
    )

    plt.title("Average Score Distribution")
    plt.xlabel("Average Score")
    plt.ylabel("Number of Students")

    plt.tight_layout()

    plt.savefig("images/average_score_distribution.png")

    plt.show()


def plot_subject_comparison(df):
    """Compare average scores across subjects."""

    subjects = [
        "math_score",
        "reading_score",
        "writing_score"
    ]

    averages = df[subjects].mean()

    plt.figure(figsize=(8, 5))

    averages.plot(kind="bar")

    plt.title("Average Score by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Average Score")

    plt.xticks(
        ticks=range(3),
        labels=["Math", "Reading", "Writing"],
        rotation=0
    )

    plt.tight_layout()

    plt.savefig("images/subject_comparison.png")

    plt.show()


def plot_performance_levels(df):
    """Show student performance categories."""

    plt.figure(figsize=(8, 5))

    sns.countplot(
        data=df,
        x="performance_level",
        order=[
            "Excellent",
            "Good",
            "Average",
            "Needs Improvement",
            "Poor"
        ]
    )

    plt.title("Student Performance Levels")
    plt.xlabel("Performance Level")
    plt.ylabel("Number of Students")

    plt.xticks(rotation=20)

    plt.tight_layout()

    plt.savefig("images/performance_levels.png")

    plt.show()


def plot_correlation(df):
    """Show correlation between numerical features."""

    numeric_columns = [
        "math_score",
        "reading_score",
        "writing_score",
        "total_score",
        "average_score"
    ]

    correlation = df[numeric_columns].corr()

    plt.figure(figsize=(9, 7))

    sns.heatmap(
        correlation,
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )

    plt.title("Student Score Correlation Heatmap")

    plt.tight_layout()

    plt.savefig("images/correlation_heatmap.png")

    plt.show()


if __name__ == "__main__":

    print("Loading dataset...")

    df = load_data()

    print("Dataset loaded successfully!")
    print("Shape:", df.shape)

    print("\nCreating visualizations...")

    plot_gender_distribution(df)

    plot_score_distribution(df)

    plot_subject_comparison(df)

    plot_performance_levels(df)

    plot_correlation(df)

    print("\nAll visualizations created successfully!")