# Normalized Discounted Cumulative Gain (NDCG)

- 순위에 가중치를 준다.
- MAP, Top K Precision/Recall 등 평가방법 보완
  - 특정 아이템에 biased된 경우
  - 이미 유명하고 잘 알려진 인기있는 아니템 또는 한 명의 사용자에 의해서 만들어진 랭킹의 경우

## NDCG

- 1에 가까울수록 좋은 랭킹
- $log_2 i$로 normalization하여 순위가 낮을수록 가중치를 감소

이제 구체적으로 수식을 살펴보자.

$$CG_p = \sum_{i=1}^p rel_i$$

- 위에서 $CG_p$에서 $rel_i$는 $i$번째 아이템과 사용자간의 관련성을 의미한다고 할 수 있다.
- 해당 추천아이템을 클릭했는지, 평점을 몇 점으로 주었는지 등 상황에 따라 구체적인 값은 달라진다.
- 하지만 이 값은 아이템의 랭킹(순서)는 고려되지 않은 값이다.

$$DCG_p = \sum_{i=1}^p \frac{rel_i}{log_2 (i+1)}$$

- $CG_p$에서는 순서를 고려하지 않았지만 $DCG_p$에서는 뒤로 갈수록 작은 가중치를 주어서 순서에 따라 차등을 두었다.
- 하지만 이 또한 사용자별로 추천 아이템의 수가 다른 경우 동등한 비교가 어렵고 이를 normalize한 값이 아래의 최종 값이다.

$$NDCG_p = \frac{DCG_p}{IDCG_p}$$

- $IDCG_p$는 가장 ideal한 추천을 했을 때, $DCG$의 값이다.
- 이를 통해 NDCG는 0~1 사이의 값을 갖게 된다.

# Precision@K

- Top-K의 결과만을 이용하여 Precision 계산

# Mean Average Precision (MAP)

- Precision@K에서 K에 다양한 값을 구하고 이를 평균낸 값

# Precision/Recall, AUC

- 분류 문제 평가 지표
