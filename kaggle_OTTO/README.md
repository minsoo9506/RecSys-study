- https://www.kaggle.com/competitions/otto-recommender-system/overview
  - session 마다 item을 click, cart, buy 정보가 있고 이 3가지를 모두 맞추는 것이 목표
  - 최종 지표는 위의 3가지 recall@20의 weight average 값
- 목표: 해당 kaggle competition의 notebook들을 따라가면서 배워보기
- 진행기간: 2022.12.18 ~ 2022.12.26

# TIL

### `glob.glob`

- 사용자가 제시한 조건에 맞는 파일명을 리스트 형식으로 반환
- `glob.glob('../input/otto-validation/*_parquet/*')` 같이 사용 가능

### Co-visitation Matrix

1. 같은 session안에서 가까운 시간대(예를 들어 < 1day)에 발생한 이벤트들을 pair로 생각해서 co-visitation matrix를 만든다. (값은 전체 session에서 해당 pair의 발생 횟수가 될 것)
2. 각 item 마다 top-20 item을 뽑아내서 예측에 이용한다.

- 따라서 해당 내용에서의 중점은 memory efficiency가 될 것이다.

### logging

- python에서 제공하는 logging을 이용하여 log를 쉽게 볼 수 있다.

```python
# logger 생성
logger = getLogger()
# log 출력 (consolg에 log 남기기)
c_handler = logging.StreamHandler()
# 로그 출력 기준 설정
c_handler.setLevel(logging.INFO)
# logger에 전달
logger.addHandler(c_handler)
# 출력
logger.info(model)
```

# notebook 따라하기

- [EDA + Baseline](./00_otto_eda_baseline.ipynb)
  - 기본적인 EDA와 데이터의 형태 파악
  - freqency를 이용한 rule-based model 모델링
- [Candidate ReRank Model (Co-visitation Matrix)](./01_candidate_rerank_model.ipynb)
  - co-visitation matrix를 빠르고 메모리 효율적으로 만드는 과정 (parquet, cudf with GPU)
- [recbole - GRU4REC](./02_recbole_GRU4REC.ipynb)
  - recbole에 구현되어 있는 GRU4REC 모델이용
- [Merlin-XGBoost ranker GPU](./03_xgboost_ranker_gpu.ipynb)

# Score

| model            | public score (weighted recall@) |
| ---------------- | ------------------------------- |
| rule-based model | 0.482                           |
| GRU4REC          | 0.544                           |
| XGBoost ranker   | 0.482                           |

# Other References

- [(Article) Transformers4Rec: A flexible library for Sequential and Session-based recommendation](https://medium.com/nvidia-merlin/transformers4rec-4523cc7d8fa8)
- [해당 데이터 EDA를 잘한 노트북](https://www.kaggle.com/code/andradaolteanu/otto-i-was-warned-this-one-is-complicated)
- [The inner workings of the lambdarank objective in LightGBM](https://ffineis.github.io/blog/2021/05/01/lambdarank-lightgbm.html)
