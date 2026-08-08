import pandas as pd
from clean_data import clean_data


def add_features(df):
    """
    Add new features to the cleaned student performance dataset.
    """

    # Make a copy
    df = df.copy()

    # Calculate total score
    df["total_score"] = (
        df["math_score"]
        + df["reading_score"]
        + df["writing_score"]
    )

    # Calculate average score
    df["average_score"] = (
        df["total_score"] / 3
    ).round(2)

    # Create performance level
    def get_performance(score):

        if score >= 80:
            return "Excellent"

        elif score >= 70:
            return "Good"

        elif score >= 60:
            return "Average"

        elif score >= 50:
            return "Needs Improvement"

        else:
            return "Poor"

    df["performance_level"] = df["average_score"].apply(
        get_performance
    )

    return df


if __name__ == "__main__":

    file_path = "data/StudentPerformance.csv"

    # Load original dataset
    df = pd.read_csv(file_path)

    print("Original shape:")
    print(df.shape)

    # Clean dataset first
    df_cleaned = clean_data(df)

    print("\nCleaned shape:")
    print(df_cleaned.shape)

    # Add features
    df_featured = add_features(df_cleaned)

    print("\nNew columns:")
    print(df_featured.columns.tolist())

    print("\nFirst 5 students:")

    print(
        df_featured[
            [
                "math_score",
                "reading_score",
                "writing_score",
                "total_score",
                "average_score",
                "performance_level"
            ]
        ].head()
    )