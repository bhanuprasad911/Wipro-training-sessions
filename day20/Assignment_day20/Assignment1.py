import numpy as np
import pandas as pd

students = [
{"name": "Alice", "score": 85},
{"name": "Bob", "score": 92},
{"name": "Charlie", "score": 78},
{"name": "David", "score": 90},
{"name": "Eva", "score": 88}
]

df = pd.DataFrame(students)
print("Mean", np.mean(df['score']))
print("Medain", np.median(df["score"]))
print("Standard deviation",df['score'].std() )
df['above_average'] = df['score']>np.mean(df['score'])

