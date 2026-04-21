import pandas as pd

def clean_data(df):
    print("\n🧹 Cleaning data...\n")

    # 1. Remove duplicates
    df = df.drop_duplicates()

    # 2. Handle missing values
    df = df.fillna({
        "Age": df["Age"].mean(),
        "Gender": "Unknown",
        "Satisfaction": df["Satisfaction"].mean(),
        "Platform": "Unknown",
        "Feedback": "No Feedback"
    })

    # 3. Convert data types
    df["Age"] = df["Age"].astype(int)
    df["Satisfaction"] = df["Satisfaction"].astype(int)

    print("✅ Data cleaned successfully!\n")
    print(df.head())

    return df
