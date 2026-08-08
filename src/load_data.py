import pandas as pd
def load_student_data(file_path):
    """
    Load student performance dataset.
    """
    df=pd.read_csv(file_path)
    return df
if __name__=="__main__":
    file_path="data/StudentsPerformance.csv"
    df=load_student_data(file_path)
    print("Dataset loaded successfully!")
    print()

    print("First 5 rows:")
    print(df.head())

    print()

    print("Dataset shape:")
    print(df.shape)

    print()

    print("Column names:")
    print(df.columns.tolist())