
import json
import csv
import pandas as pd

with open('data.json', encoding='utf-8') as f:
    df = pd.read_json(f)

df.to_csv('csvfile.csv', encoding='utf-8', index=False)

print(df.head())
