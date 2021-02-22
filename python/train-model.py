import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors

def train_model():
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

  print(df.head())

  model_knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=20, n_jobs=-1)
  model_knn.fit(df.to_numpy())

  # This is throwing an error – trying to follow this tutorial: https://heartbeat.fritz.ai/recommender-systems-with-python-part-ii-collaborative-filtering-k-nearest-neighbors-algorithm-c8dcd5fd89b2
  distances, indicies = model_knn.kneighbors(df['2231'], n_neighbors=5)

if __name__ == "__main__":
  train_model()