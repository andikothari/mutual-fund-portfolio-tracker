import pandas as pd
from pathlib import Path
from typing import Dict, Any

def parse_csv(filepath: str | Path, config: Dict[str, Any]) -> pd.DataFrame:
    """
    Parse CSV with vendor-specific config.
    
    Args:
        filepath: Path to CSV file
        config: YAML config with encoding, columns, etc.
    
    Returns:
        Raw DataFrame with original columns
    """
    filepath = Path(filepath)
    if not filepath.exists():
        raise FileNotFoundError(f"CSV not found: {filepath}")
    
    # Use config encoding, fallback to UTF-8
    encoding = config.get("encoding", "utf-8-sig")
    
    df = pd.read_csv(
        filepath,
        encoding=encoding,
        low_memory=False,
        dtype_backend="pyarrow"  # Modern type inference
    )
    
    print(f"📊 Loaded {len(df)} rows, {len(df.columns)} columns")
    print("Columns:", list(df.columns))
    print("\nFirst 3 rows:\n", df.head(3))
    
    return df
