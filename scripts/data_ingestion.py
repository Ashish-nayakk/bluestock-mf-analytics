import pandas as pd
from pathlib import Path

data_path = Path("data/raw")

for file in data_path.glob("*.csv"):
    df = pd.read_csv(file)

    print("\n" + "="*50)
    print(file.name)

    print("Shape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nDtypes:")
    print(df.dtypes)

    print("\nHead:")
    print(df.head())