import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def cos_sim_matrix(a: pd.DataFrame, b: pd.DataFrame) -> pd.DataFrame:
    """get cosine similarity matrix

    Parameters
    ----------
    a : pd.DataFrame
        _description_
    b : pd.DataFrame
        _description_

    Returns
    -------
    pd.DataFrame
        n * n cosine similarity matrix
    """
    sim_val = cosine_similarity(a.values, b.values)
    cos_sim_df = pd.DataFrame(data=sim_val, columns=a.index, index=a.index)
    return cos_sim_df
