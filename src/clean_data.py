import pandas as pd


def clean_data(df):
    """
    Clean the student performance dataset.
    """

    # Copy original data
    df = df.copy()

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Standardize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Remove extra spaces from text columns
    text_columns = df.select_dtypes(include="object").columns

    for column in text_columns:
        df[column] = df[column].str.strip()

    # Remove missing values
    df = df.dropna()

    return df


if __name__ == "__main__":

    file_path = "data/StudentPerformance.csv"

    # Load dataset
    df = pd.read_csv(file_path)

    print("Before cleaning:")
    print("Shape:", df.shape)

    # Clean dataset
    df_cleaned = clean_data(df)

    print("\nAfter cleaning:")
    print("Shape:", df_cleaned.shape)

    print("\nMissing values:")
    print(df_cleaned.isnull().sum())

    print("\nColumn names:")
    print(df_cleaned.columns.tolist())