# 모델기반

- 머신러닝을 잘 활용
- 유사성만을 이용하는 것이 아닌 데이터의 패턴을 학습
- 데이터의 잠재적 특성을 파악

# Rule-Based collaborative filtering (skip)

- association rule

# Latent Factor collaborative filtering

## Matrix Factorization

- latent factor model을 구현하는 방법
- user-item matrix를 분해
- 위의 matrix에서 비어있는 곳을 채우는 matrix completion 문제
- SVD류, GD, ALS 등의 방법으로 MF를 진행한다.
- 관측된 데이터를 사용, 즉 train, test의 개념이 없다.

### objective function

- $x_u, y_i$: user와 item의 latent vector
- $r_{ui}$: user $u$가 item $i$에 부여한 실제 rating 값
- $\hat{r_{ui}}=x_u^T y_i$: user $u$가 item $i$에 부여할 rating 예측값
- $\lambda (||x_u||^2 + ||y_i||^2)$: regularization term
  - sparse한 matrix이기에 값을 갖는 rating에 overfitting되지 않도록

$$min \sum (r_{ui} - x_u^T y_i)^2 + \lambda (||x_u||^2 + ||y_i||^2)$$

### optimization - SGD

- $x_u, y_i$를 update
- error term: $e_{ui} = r_{ui} - x_i^T y_u$

$$x_u \leftarrow x_u + \gamma (e_{ui} \cdot y_i - \lambda \cdot x_u)$$
$$y_i \leftarrow y_i + \gamma (e_{ui} \cdot x_u - \lambda \cdot y_i)$$

### optimization - ALS

- $x_u$와 $y_i$ 둘 중 하나를 고정하고 식을 quadratic식으로 최적화 문제를 풀 수 있다.
- $x_u$와 $y_i$를 번갈아 고정시키면서, least-square 문제를 푼다.
- 병렬처리에 용이하다.
- Implicit feedback이 처리시에 유리하다.
  - dense하기에 연산량이 많아지는에 이를 빠르게 계산할 수 있다.

### advance MF

1. bias 추가: 개별 특성을 더 표현

- $b_{ui} = \mu + bu_i + b_u$
  - $\mu$: 모든 item의 평균
  - $b_i$: 모든 item의 평균과 item $i$의 차이
  - $b_u$: 모든 user의 평균과 user $u$의 차이

$$min \sum (r_{ui} -b_{ui} - x_u^T y_i)^2 + \lambda (||x_u||^2 + ||y_i||^2 + b_i^2 + b_u^2)$$

2. additional input sources: 추가 정보를 활용한 모델링

- $\sum_{i \in N(u)} y_i$: user $u$의 item $i$에 대한 implicit feedback
  - $N(u)$: 전체 item에 대한 user $u$의 implicit feedback
- $\sum_{a\in A(a)}x_a$: user $u$의 personal or non-item related information
  - 성별, 나이, 주소 등

$$\hat{r_{ui}} = \mu + b_i + b_u + x_u^T [y_i + |N(u)|^{-0.5}\sum_{i \in N(u)} y_i \sum_{a \in A(u)}x_a]$$

3. Temporal Dynamics

- 데이터를 시간의 따른 변화를 반영
- $t$: 시간
- $b_i(t)$: item $i$의 인기도가 시간의 흐름에 따라 변하는 경우
- $b_u(t)$: user $u$가 시간이 흐르면서 baseline rating이 변하는 경우
- $x_i^Ty_u(t)$: 시간이 흐르면서 취향의 변화

$$\hat{r_{ui}(t)} = \mu + b_i(t) + b_u(t) + x_i^Ty_u(t)$$

4. input with varying confidence levels

- 데이터가 동일한 가중치 또는 동일한 신뢰도가 아닌 경우 고려
  - 예를 들어, 대규모 광고를 받은 item이 인기가 많은 경우
- implicit feedback 데이터에서 user가 실제로 선호하는지 판단하기 어려운 경우
- $c_{ui}$: $r_{ui}$에 대한 가중치(신뢰도)

$$min \sum cU{ui}(r_{ui} -b_{ui} - x_u^T y_i)^2 + \lambda (||x_u||^2 + ||y_i||^2 + b_i^2 + b_u^2)$$
