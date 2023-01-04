한줄요약: Wide & Deep learning—jointly trained wide linear models and deep neural networks—to combine the benefits of memorization and generalization for recommender systems.

- 추천시스템은 input(user, contextual information)을 넣으면 특정 목적(클릭, 구매 등)에 기반한 list of ranked items을 output으로 보내주는 것이다.
- 해당논문은 memorization + generalization을 동시에 잘하려고 했다.
  - memorization: usually more topical and
    directly relevant to the items on which users have already
    performed actions
  - generalization: tends to improve the diversity of the recommended
    items, explores new feature combinations that have never or rarely occurred in the past
- 추천하려는 앱이 너무 많기 때문에 사전에 필터링하는 작업을 통해서 input set을 만들어서 ranking을 한다.

# 모델

[논문 Figure1](https://arxiv.org/pdf/1606.07792.pdf)을 보면 된다.

## The Wide Component

wide component에서는 memorization의 역할을 한다.

- Generalized Linear model
  - $y$: prediction (유저의 행동과 관련된 값)
  - $x$: raw input feature & cross-product feature

$$y=w^Tx+b$$

### cross-product feature

- feature interaction 반영
- non-linearity 반영

$$\phi_k (x) = \prod_{i=1}^d x_i^{c_{ki}}, \;c_{ki} \in \{ 0,1 \}$$

- 위의 값은 cross-product feature의 $k$번째 요소

예를 들어서, `gender=남자, age=20대` 라는 cross-product feature는 해당 row의 `gender=남자`이고 `age=20대`인 경우 1의 값을 갖는다. (interaction term인 것이다)

## The Deep Component

deep component에서는 generalization의 역할을 한다.

- sparse feature를 input으로 embedding layer에 넣고 이후에는 fully-connected layer를 통해서 학습한다.

## Joint Training

- wide, deep 부분을 jointly 학습했다.
- 독립적으로 훈련하는 ensemble방법에 비해서 jointly 학습하면 서로의 약점을 보완하고 모델 사이즈도 더 작아진다.
- 최종 model's prediction은:

$$P(Y=1|x) = \sigma(w_{wide}^T[x,\phi(x)] + w_{deep}^T a + b)$$

# 시스템

pipline은 data generation, model training, model serving 3가지로 구성되어 있다.
