def analyze_data(df):
    print("\n📊 Analyzing data...\n")

    # 1. Average satisfaction
    avg_satisfaction = df["Satisfaction"].mean()
    print(f"⭐ Average Satisfaction: {avg_satisfaction:.2f}")

    # 2. Gender distribution
    gender_counts = df["Gender"].value_counts()
    print("\n👥 Gender Distribution:\n", gender_counts)

    # 3. Platform usage
    platform_counts = df["Platform"].value_counts()
    print("\n📱 Platform Usage:\n", platform_counts)

    # 4. Age statistics
    print("\n🎂 Age Statistics:\n", df["Age"].describe())

    return {
        "avg_satisfaction": avg_satisfaction,
        "gender_counts": gender_counts,
        "platform_counts": platform_counts
    }
