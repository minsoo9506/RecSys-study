from typing import Tuple

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

import torch
from torch.utils.data import dataset


def read_ratings_data(
    data_path: str, test_size: float
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """read ratings data

    Parameters
    ----------
    data_path : str
        data path
    test_size : float
        _description_

    Returns
    -------
    Tuple[pd.DataFrame, pd.DataFrame]
        return train, valid dataframe
    """
    df = pd.read_csv(data_path)
    train_df, valid_df = train_test_split(df, test_size=test_size, random_state=0)
    return train_df, valid_df


class NCFMakeData:
    def __init__(self, data_path: str):
        """generate train, valid data in used in NCF model

        Parameters
        ----------
        data_path : str
            data path
        """
        self.train_df, self.valid_df = read_ratings_data(data_path, 0.2)

        self.unique_users = self.train_df["user"].unique()
        self.num_unique_users = len(self.unique_users)
        self.unique_movies = self.train_df["movie"].unique()
        self.num_unique_movies = len(self.unique_movies)

        # embedding layer를 사용하기 때문에
        self.user_to_idx = {
            original: idx for idx, original in enumerate(self.unique_users)
        }
        self.movie_to_idx = {
            original: idx for idx, original in enumerate(self.unique_movies)
        }

        # train에 있는 대상들로만 valid 남겨서 모델 학습시 사용
        self.valid_df = self.valid_df[
            self.valid_df["user"].isin(self.unique_users)
            & self.valid_df["movie"].isin(self.unique_movies)
        ]

    def generate_train_df(self) -> Tuple[pd.DataFrame, np.ndarray]:
        """generate train dataset

        Returns
        -------
        Tuple[pd.DataFrame, np.ndarray]
            X_train, y_train
        """
        X_train = pd.DataFrame(
            {
                "user": self.train_df["user"].map(self.user_to_idx),
                "movie": self.train_df["movie"].map(self.movie_to_idx),
            }
        )
        y_train = self.train_df["rate"].astype(np.float32)

        return X_train, y_train

    def generate_valid_df(self) -> Tuple[pd.DataFrame, np.ndarray]:
        """generate valid dataset

        Returns
        -------
        Tuple[pd.DataFrame, np.ndarray]
            X_valid, y_valid
        """
        X_valid = pd.DataFrame(
            {
                "user": self.valid_df["user"].map(self.user_to_idx),
                "movie": self.valid_df["movie"].map(self.movie_to_idx),
            }
        )
        y_valid = self.valid_df["rate"].astype(np.float32)

        return X_valid, y_valid


class NCFDataset(dataset):
    def __init__(self, X: pd.DataFrame, y: np.ndarray):
        """_summary_

        Parameters
        ----------
        X : pd.DataFrame
            _description_
        y : np.ndarray
            _description_
        """
        X, y = np.array(X), np.array(y)
        # torch.Tensor()는 새 메모리를 할당하지만 torch.from_numpy()는 그대로 사용한다고 함
        self.X = torch.from_numpy(X)
        self.y = torch.from_numpy(y)

    def __len__(self) -> int:
        """return len of data

        Returns
        -------
        int
            len of data
        """
        return len(self.X)

    def __getitem__(self, idx: int) -> Tuple[torch.Tensor, torch.Tensor]:
        """return X, y

        Parameters
        ----------
        idx : int
            data index

        Returns
        -------
        Tuple[torch.Tensor, torch.Tensor]
            X, y
        """
        return self.X[idx, :], self.y[idx]
