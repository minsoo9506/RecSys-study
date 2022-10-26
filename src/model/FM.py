import numpy as np


class FactorizationMachine:
    def __init__(self):
        pass
        # weight들

    def _predict(self, X, w0, w, v, n_factors, i):
        data = X.data
        indices = X.indices
        indptr = X.indptr
        summed = np.zeros(n_factors)
        summed_squared = np.zeros(n_factors)

        # bias
        pred = w0
        # linear: w * x
        for idx in range(indptr[i], indptr[i + 1]):
            col_loc = indices[idx]
            pred += w[col_loc] * data[col_loc]

        # factor
        for factor in range(n_factors):
            for idx in range(indptr[i], indptr[i + 1]):
                col_loc = indices[idx]
                term = v[factor, col_loc] * data[idx]
                summed[factor] += term
                summed_squared[factor] += term**2

            pred += 0.5 * (summed[factor] ** 2 - summed_squared[factor])

        return pred, summed

    def _sgd(self):
        pass

    def fit(self):
        pass
