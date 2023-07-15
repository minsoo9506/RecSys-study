# Contents based filtering algorithm

- 유저가 높은 평점을 주거나 큰 관심을 갖는 아이템 i와 유사한 아이템 j를 추천
- 유저가 과거에 경험했던 아이템 중 비슷한 아이템을 현재 시점에 추천

### 장점

- 다른 유저의 데이터가 필요하지 않다.
- 추천할 수 있는 아이템의 범위가 넓다.
- 추천하는 이유를 이해하기 쉽다.

### 단점

- 유사도를 계산할 적절한 feature를 찾기 어렵다.
- 새로운 유저를 위한 추천이 어렵다. (cold start problem)
- 선호하는 특성을 가진 항목을 반복 추천한다. 다른 종류나 새로운 아이템이 추천되지 않는다.

### 중요한 점

- 컨텐츠의 내용을 분석하는 알고리즘이 중요 (feature extraction)
- 적절한 컨텐츠 데이터를 사용

### 어떤 정보를 이용?

- Item profile
  - = feature extraction = vectore representation
- User profile
  - 데이터로부터 유저 성향 파악
    - explicit, implicit feedback 등
    - 사용자가 가지고 있는 아이템 특성 가중치의 평균값을 활용하기도 한다.

### 비슷한 컨텐츠를 찾는 방법

- Cosine similarity
  - -1 ~ 1 사이의 값
  - 두 벡터의 유사도를 측정

$$cs = \frac{A \cdot B}{||A|| ||B||}$$

- Jaccard similarity
  - 집합의 개념을 이용한 유사도 계산
  - 두 집합의 유사도는 얼마나 많은 아이템이 겹치는지로 판단

$$J(A,B) = \frac{|A \cap B|}{|A \cup B|}$$

- Pearson similarity
  - 두 벡터의 상관관계를 계산

$$r_{xy} = \frac{\sum (X_i - \bar{X})(Y_I - \bar{Y})}{\sqrt{\sum(X_i - \bar{X})^2} \sqrt{\sum(Y_i - \bar{Y})^2}}$$

# Nearest Neighbor algorithm

- 데이터(아이템 또는 유저)로부터 거리가 가까운 k개의 다른 데이터를 선택하는 알고리즘
- 거리를 측정할 때, 어떤 metric을 사용할지 고민
- k를 몇으로 할지 고민
- Model-based learning은 아니라고 할 수 있다.

### 장점

- 단순하고 효율적이다.
- 수치 기반 데이터에서는 좋은 성능을 보이기도 한다.

### 단점

- 카테고리 데이터는 처리하기 어렵다.
- feature의 수가 많은 데이터는 처리속도가 느리고 정확도도 떨어진다.
- feature마다 스케일이 비슷해야한다.
- 적절한 k를 선택하는 것이 어렵다.

### 주의해야할 점

- feature들의 스케일
- 데이터 간의 거리 측정 효율화
- 공간 상에서 데이터의 representation 상태 확인 필요

# Naive Bayes algorithm

- feature끼리 서로 독립 가정한다.
- continuous보다 discrete feature가 더 적절하다.

$$P(Class_j | x) = \frac{P(x|Class_j)\cdot P(Class_j)}{P(x)}$$

$$P(x|Class_j) = P(x_1|Class_j) \cdot P(x_2|Class_j) ... P(x_d|Class_j)$$

# TF-IDF

Document-Word matrix가 있다고 하자. matrix의 값은 해당 Document에 해당 Word가 몇번 등장했는지 나타낸다. 거기에 IDF값을 곱하면 Document TF-IDF representation을 얻을 수 있다.

- TF: Word $w$가 Document $d$에 등장한 빈도수
- DF: Word $w$가 등장한 Document 수

$$TF(w,d) = \frac{\text{문서 d에서 등장한 단어 w의 수}}{\text{문서 d에서 등장한 모든 단어의 수}}$$

$$IDF(w) = \frac{\text{전제 문서 수}}{\text{단어 w가 등장한 문서 수 (DF)}}$$

$$TF-IDF(w,d) = TF(w,d) \cdot IDF(w)$$
