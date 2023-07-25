### 보상의 2가지 형태
- 일정한 보상 (stationary reward)
  - 언제나 동일한 상수 값의 보상을 주는 경우
- 변칙적 보상 (non-stationary reward)
  - 다양한 패턴 혹은 분포를 따라 보상이 변화하는 경우
  - 분포가 시간의 흐름에 따라 변화

### 탐색과 활용
- 탐험 (exploration)
- 활용 (exploitation)

### Greedy 알고리즘
- reward를 평균내어 가장 큰 bandit을 계속 이용

### $\epsilon$-Greedy 알고리즘
- exploration을 하려고 하는 것
- 1 - $\epsilon$의 확률로는 평균 reward가 가장 큰 경우, $\epsilon$의 확률로는 random action

### UCB(upper confidence bound)
- 너무 선택되지 않은 경우, 해당 보상에 대한 신뢰구간이 넓을 것이고 따라서 UCB가 큰 경우를 선택한다.