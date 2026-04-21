
import matplotlib.pyplot as plt
import os
def create_visuals(df):
    print("\n📊 Generating visualizations...\n")

    # Create output folder if it doesn't exist
    os.makedirs("../output", exist_ok=True)

    # 1. Gender Distribution (Bar Chart)
    df["Gender"].value_counts().plot(kind='bar')
    plt.title("Gender Distribution")
    plt.xlabel("Gender")
    plt.ylabel("Count")
    plt.savefig("../output/gender_distribution.png")
    plt.clf()

    # 2. Platform Usage (Pie Chart)
    df["Platform"].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title("Platform Usage")
    plt.ylabel("")
    plt.savefig("../output/platform_usage.png")
    plt.clf()

    # 3. Age Distribution (Histogram)
    df["Age"].plot(kind='hist', bins=10)
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.savefig("../output/age_distribution.png")
    plt.clf()

    print("✅ Visualizations saved in output folder!")