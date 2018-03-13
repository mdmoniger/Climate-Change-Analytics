import pandas as pd

df = pd.read_csv('master.csv')
df = df[df['oxygen']!=-9999]
df = df[df['temperature']!=-9999]
# df = df[df['depth']<20]
