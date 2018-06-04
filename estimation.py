import pandas as pd
import numpy as np


def describe(graph_name):
  df_graph = pd.read_csv(graph_name)
  graph_column = df_graph.iloc[:, 1]
  graph_values = graph_column.values.reshape(-1, 1)
  graph_sigma = (graph_values.T @ graph_values) / (graph_values.shape[0] - 1)
  graph_std = np.sqrt(graph_sigma)
  print(graph_sigma, graph_std, graph_column.describe())


describe('config/log/Graph1.txt')
describe('config/log/Graph2.txt')
