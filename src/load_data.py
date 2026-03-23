import pandas as pd
import sys

print("Script started!", flush=True)

# File path
file_path = "data/raw/sample_conversations.csv"
print(f"Loading from: {file_path}", flush=True)

try:
    # Load dataset
    df = pd.read_csv(file_path)
    
    # Print basic info
    print("Dataset loaded successfully!\n", flush=True)
    
    print("Shape (rows, columns):", df.shape, flush=True)
    
    print("\nColumns:", flush=True)
    print(df.columns.tolist(), flush=True)
    
    print("\nFirst 5 rows:", flush=True)
    print(df.head(), flush=True)
    
except Exception as e:
    print(f"ERROR: {e}", file=sys.stderr, flush=True)
    import traceback
    traceback.print_exc()