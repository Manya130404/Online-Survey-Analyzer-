import pandas as pd

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)

        print("\n✅ Data Loaded Successfully!\n")
        print(df.head())

        return df

    except Exception as e:
        print("❌ Error loading data:", e)
        return None