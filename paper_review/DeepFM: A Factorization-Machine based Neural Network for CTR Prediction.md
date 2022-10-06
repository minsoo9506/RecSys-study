- CTR 예측 모델
- Low, High-order interaction 모두 학습 가능
- Factorization Machine과 Deep Learning의 장점을 합친 모델
- feature engineering 없이 raw feature를 그대로 사용 가능

# 모델

[논문 Figure1](https://fastcampus.co.kr/courses/203078/clips/)을 통해서 어렵지 않게 모델의 형태를 이해할 수 있다.

먼저, input data의 형태부터 알아보자.

- 각 instance들은 $(x,y)$로 표시 할 수 있다.
- 여기서 $y$는 클릭여부를 나타내므로 0 또는 1의 값을 가진다.
- 논문에서는 $x$를 field들로 이루어져있다고 설명한다. 각 field는 하나의 feature를 의미한다.
- 이는 유저, 아이템, 기타 변수들로 이루어졌있다. 따라서 상당히 high dimension이고 sparse하다.

DeepFM은 FM component와 Deep component로 이루어져있다.

### FM

FM component는 factorization machine을 의미한다.

$$y_{FM} = \langle w,x \rangle + \sum_{j_1=1}^d \sum_{j_2 = j_1 + 1}^d  \langle V_i,V_j \rangle x_{j_1} \cdot x_{j_2}$$

### Deep

여기서는 high-order feature interaction을 feed-forward nn으로 학습한다.
