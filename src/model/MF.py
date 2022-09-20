# reference: https://github.com/albertauyeung/matrix-factorization-in-python

import numpy as np


class MF:
    def __init__(
        self, matrix: np.ndarray, latent_dim: int, alpha: float, beta: float, iters: int
    ):
        """matrix factorization with SGD

        Parameters
        ----------
        matrix : np.ndarray
            user-item matrix
        latent_dim : int
            latent dimension
        alpha : float
            learning rate
        beta : float
            regularization parameter
        iters : int
            num of iterations
        """
        self.matrix = matrix
        self.num_users, self.num_items = matrix.shape
        self.latent_dim = latent_dim
        self.alpha = alpha
        self.beta = beta
        self.iters = iters

    def train(self):
        """train MF"""

        # initialize user and item latent feature matrix
        self.U = np.random.normal(
            scale=1.0 / self.latent_dim, size=(self.num_users, self.latent_dim)
        )
        self.I = np.random.normal(
            scale=1.0 / self.latent_dim, size=(self.num_items, self.latent_dim)
        )

        # initialize the bias
        self.b_u = np.zeros(self.num_users)
        self.b_i = np.zeros(self.num_items)
        self.b = np.mean(self.matrix[np.where(self.matrix != 0)])

        # create a list of train sample: not zero
        self.samples = [
            (i, j, self.matrix[i, j])
            for i in range(self.num_users)
            for j in range(self.num_items)
            if self.matrix[i, j] != 0
        ]

        # SGD
        for i in range(self.iters):
            np.random.shuffle(self.samples)
            self._optim_sgd()
            mse = self._get_rmse()
            print(f"Iteration: {i + 1}; train_mse = {mse:.5f}")

    def _get_rmse(self):
        """get rmse

        Returns
        -------
        float
            rmse
        """
        xs, ys = self.matrix.nonzero()
        predicted = self._get_current_matrix()
        mse = np.mean(np.power(self.matrix[xs, ys] - predicted[xs, ys], 2))
        rmse = np.sqrt(mse)
        return rmse

    def _get_current_matrix(self):
        """get current updating(predict) matrix

        Returns
        -------
        np.ndarray
            current predict matrix
        """
        return (
            self.b
            + self.b_u[:, np.newaxis]
            + self.b_i[
                np.newaxis :,
            ]
            + self.U.dot(self.I.T)
        )

    def _optim_sgd(self):
        pass

    def get_rating(self, i, j):
        pass

    def show_full_matrix(self):
        pass
