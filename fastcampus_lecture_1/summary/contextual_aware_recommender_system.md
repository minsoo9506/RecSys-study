- Context-Aware Recommender System
  - 유저와 아이템 사이의 관계 뿐만 아니라 상황 정보도 포함한 포괄적인 추천시스템
  - 도메인 지식을 잘 활용할 수 있다.
- context
  - context는 예를 들어 시간, 장소, 메타정보 등이 있다.
  - context는 explicit, implicit 모두 존재한다.
  - context는 시간의 흐름에 따라 변할수도 그대로 일 수도 있다.

# Contextual Pre-filtering

- context 정보를 활용하여 가장 연관된 user-item 데이터를 만들고 이를 이용하여 추천한다.
- 즉, context가 query의 역할을 하는 것이다.
- context generalization도 중요하다.
  - 너무 specific하면 sparsity 문제 발생

# Contextual Post-filtering

- 추천 결과를 context 정보를 활용하여 filter 또는 adjust한다.

# Contextual Modeling

- 기존의 2d가 아니라 N-dim의 데이터로 확장하여 모델링한다.
  - user, item, context
- example
  - Context-aware SVM
  - Tensor Factorization
  - Factorization Machine
