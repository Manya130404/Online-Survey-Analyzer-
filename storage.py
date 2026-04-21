def save_data(df):
    print("\n💾 Saving processed data...\n")

    df.to_csv("../output/processed_data.csv", index=False)

    print("✅ Processed data saved!")