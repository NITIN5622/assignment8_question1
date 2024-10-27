import pandas as pd
df = pd.read_csv('email.csv')
df = df.sample(frac=1).reset_index(drop=True)

df.to_csv('email_1.csv', index=False)