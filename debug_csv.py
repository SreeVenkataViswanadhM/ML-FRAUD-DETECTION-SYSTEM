import pandas as pd

try:
    data = pd.read_csv('data/creditcard.csv')
    print("CSV loaded successfully")
    print(f"Shape: {data.shape}")
except Exception as e:
    print(f"Error: {e}")
    # Try to find the problematic line
    with open('data/creditcard.csv', 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            fields = line.strip().split(',')
            if len(fields) != 31:
                print(f"Line {i}: {len(fields)} fields - {line.strip()}")
