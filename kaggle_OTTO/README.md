- https://www.kaggle.com/competitions/otto-recommender-system/overview
  - session 마다 item을 click, cart, buy 정보가 있고 이 3가지를 모두 맞추는 것이 목표
- 해당 kaggle competition의 노트북들을 따라가면서 배워보기
- 2022.12.18 ~

# Learn

### `glob.glob`

- 사용자가 제시한 조건에 맞는 파일명을 리스트 형식으로 반환
- `glob.glob('../input/otto-validation/*_parquet/*')` 같이 사용 가능

### Co-visitation Matrix

1. 같은 session안에서 가까운 시간대(예를 들어 < 1day)에 발생한 이벤트들을 pair로 생각해서 co-visitation matrix를 만든다. (값은 전체 session에서 해당 pair의 발생 횟수가 될 것)
2. 각 item 마다 top-20 item을 뽑아내서 예측에 이용한다.

- 따라서 해당 내용에서의 중점은 memory efficiency가 될 것이다.

# notebook description

- [EDA + Baseline](./00_otto-eda-baseline.ipynb)
  - 기본적인 EDA와 데이터의 형태 파악
  - freqency를 이용한 rule-based model 모델링
- [Candidate ReRank Model (Co-visitation Matrix)](./01_candidate-rerank-model.ipynb)
  - co-visitation matrix를 빠르고 메모리 효율적으로 만드는 과정 (parquet, cudf with GPU)
- gpu MF 모델
- rank xgboost 모델
- transformer4rec아니 gru4rec 모델

# Score

| model                | public score (weighted recall@) |
| -------------------- | ------------------------------- |
| rule-based model     | 0.482                           |
| Co-visitation matrix |                                 |

# Reference

- [(Article) Transformers4Rec: A flexible library for Sequential and Session-based recommendation](https://medium.com/nvidia-merlin/transformers4rec-4523cc7d8fa8)
