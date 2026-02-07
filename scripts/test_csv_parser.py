from pathlib import Path
from src.ingest.csv_parser import parse_csv

def main():
    # Minimal config for now - we'll add YAML later
    config = {
        "encoding": "utf-8-sig",
        "header": 0
    }
    
    filepath = Path("data/raw/tickertape_sample.csv")
    
    try:
        df = parse_csv(filepath, config)
        print("\n✅ CSV Parser works!")
        print(f"Shape: {df.shape}")
        print("\nColumn names:")
        for col in df.columns:
            print(f"  - '{col}'")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()