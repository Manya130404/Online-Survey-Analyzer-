from src.ingestion import load_data
from src.processing import clean_data
from src.analysis import analyze_data
from src.visualization import create_visuals
from src.storage import save_data

def run_pipeline():
    file_path = "data/survey.csv"

    df = load_data(file_path)

    if df is not None:
        df = clean_data(df)
        analyze_data(df)
        create_visuals(df)
        save_data(df)

if __name__ == "__main__":
    run_pipeline()