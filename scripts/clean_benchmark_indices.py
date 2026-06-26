import pandas as pd

bench = pd.read_csv("data/raw/10_benchmark_indices.csv")

bench["date"] = pd.to_datetime(bench["date"])

bench = bench.sort_values(["index_name", "date"])

bench = bench.drop_duplicates()

bench = bench[bench["close_value"] > 0]

bench.to_csv(
    "data/processed/clean_benchmark_indices.csv",
    index=False
)

print("Saved clean_benchmark_indices.csv")