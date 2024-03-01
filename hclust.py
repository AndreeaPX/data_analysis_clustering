import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import linkage

class hclust():
    def __init__(self,t,variables,method="ward"):
        self.x = t[variables].values
        self.h = linkage(self.x, method=method)

    def get_partition(self, k=None):
        junction_num = self.h.shape[0]
        n = junction_num + 1
        if k is None:
            k_max = np.argmax(self.h[1:, 2] - self.h[:(junction_num - 1), 2])
            k = junction_num - k_max
        else:
            k_max = junction_num - k
        self.k = k
        self.threshold = (self.h[k_max, 2] + self.h[k_max + 1, 2]) / 2
        c = np.arange(n)
        for j in range(junction_num - k + 1):
            k1 = self.h[j, 0]
            k2 = self.h[j, 1]
            c[c == k1] = n + j
            c[c == k2] = n + j
        codes = pd.Categorical(c).codes
        return np.array(["c" + str(i + 1) for i in codes])