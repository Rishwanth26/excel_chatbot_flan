import pandas as pd

def load_and_clean_excel(uploaded_file) -> pd.DataFrame:
    df = pd.read_excel(uploaded_file)
    # Normalize column names
    df.columns = [
        ''.join(c if c.isalnum() else '_' for c in col.strip().lower())
        for col in df.columns
    ]
    # Try to convert columns to numeric or datetime where possible
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except Exception:
            pass
        try:
            df[col] = pd.to_datetime(df[col])
        except Exception:
            pass
    return df
