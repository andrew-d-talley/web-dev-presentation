import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from collections import defaultdict

df = pd.read_csv('./classes.csv')
df = pd.DataFrame(df.to_numpy().flatten())
df[0] = df[0].astype(str)

df = df[0].str.split(", ", expand=True).fillna("")

all_names = set()
all_names.update(df[0].unique())
all_names.update(df[1].unique())
all_names.update(df[2].unique())
all_names.remove('')

new_df = pd.DataFrame()

for name in all_names:
  new_df[name] = df.apply(lambda x: x[0] == name or x[1] == name or x[2] == name, axis=1).head(20)

df = new_df

model = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=20, n_jobs=-1)
model.fit(df.T.to_numpy())

def run_model(classes):
  mult_distances, mult_indicies = model.kneighbors([df.T.loc[c] for c in classes], n_neighbors=5)

  results = defaultdict(lambda: 1)

  for distances, indices in zip(mult_distances, mult_indicies):
    for distance, index in zip(distances, indices):
      results[index] *= distance

  values = sorted(results.items(), key=lambda k: k[1])
  print(values)
  print(df.columns)

  return [df.columns[ind] for ind, dist in values if dist < 1 and df.columns[ind] not in classes]

if __name__ == "__main__":
  print(run_model(['2201', '2212']))