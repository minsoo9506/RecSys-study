from typing import List

import numpy as np
import torch
import torch.nn as nn


class EmbdeddingFeature(nn.Module):
    def __init__(self, field_dim_list: List[int], embed_dim: int):
        """get embedding feature in each feild

        Parameters
        ----------
        field_dim_list : List[int]
            _description_
        embed_dim : int
            _description_
        """
        super().__init__()
        self.embedding = nn.Embedding(np.sum(field_dim_list), embed_dim)
        self.offsets = np.array((0, *np.cumsum(field_dim_list)[:-1]))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """_summary_

        Parameters
        ----------
        x : torch.Tensor
            x input feature

        Returns
        -------
        torch.Tensor
            embedding of each fields
        """
        # |x| = (batch_size, field_dim)
        x = x + x.new_tensor(self.offsets).unsqueeze(0)  # x.new_tensor: tensor 복사
        return self.embedding(x)


class Degree2InteractionTerm(nn.Module):
    def __init__(self):
        """interaction term in Factorization Machine (degree=2)"""
        super().__init__()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """_summary_

        Parameters
        ----------
        x : torch.Tensor
            output of class EmbeddingFeature

        Returns
        -------
        torch.Tensor
            _description_
        """
        # |x| = (batch_size, field_dim, embed_dim)
        square_of_sum = torch.sum(x, dim=1)
        sum_of_square = torch.sum(x**2, dim=1)
        out = square_of_sum - sum_of_square
        out = torch.sum(out, dim=1, keepdim=True)
        # |out| = (batch_size, 1) ? 확인필요
        return 0.5 * out
