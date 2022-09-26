from typing import List

import torch
import torch.nn.functional as F
from torch import nn, optim


class NeuralMatrixFactorization(nn.Module):
    def __init__(
        self,
        num_users: int,
        num_items: int,
        gmf_emb_dim: int,
        mlp_emb_dim: int,
        mlp_hidden_dims_list: List[int],
    ):
        super().__init__()
        self.gmf_user_emb = nn.Embedding(num_users, gmf_emb_dim)
        self.gmf_item_emb = nn.Embedding(num_items, gmf_emb_dim)
        self.mlp_user_emb = nn.Embedding(num_users, mlp_emb_dim)
        self.mlp_item_emb = nn.Embedding(num_items, mlp_emb_dim)

        # MLP layer들 생성 구현
        # 마지막 NeuMF layer 구현
