# representation learning

## 아이템 임베딩
### PinSage: a new graph convolutional neural network for web-scale recommender systems 2018
- random walk gcn 방법론, pin(아이템) 임베딩
- 사용
  - 홈 피드 추천에서 reranking feature로 사용
  - related pin ads에서 retrieval로 사용

## 유저임베딩
### PinnerSage: multi-modal user embedding framework for recommendations at pinterest 2020
- 다양한 관심사를 표현하기 위해서 여러 개의 임베딩이 필요
- 이를 위해 군집화를 이용
- 유저가 사용한 아이템들을 군집화하고 각 군집들의 임베딩값들과 유사한 아이템 추천
  - 아이템 임베딩은 pinsage로 구한 임베딩 사용
  - 그렇다면 클러스터의 임베딩은? Medoid 사용, 클러스터에 속한 특정 아이템의 임베딩으로 사용
- retrieval
  - 클러스터별로 importance 점수를 기반으로 3개를 sampling -> 이는 기반으로 ANN
- 유저의 장기, 단기 관심
  - 최근 90일치 (daily batch)
  - 당일 최근 20개 액션 (online)

## 검색어 임베딩
### SearchSage: learning search query representations at pinterest
- 단어 기반의 검색이 아닌 의미 기반의 검색을 추가하기 위해
- 서로 다른 entity를 같은 임베딩 공간에 넣는 방법?
  - 이미 만들어진 entity가 있으면
    - avg, sum
    - clustering
    - metric learning
  - 처음부터 같이 임베딩 학습
    - two-tower
- 해당 논문은 이미 만들어진 pin 임베딩(by PinSage)을 이용해서 query를 입베딩한다.
- two-tower를 사용하고
  - pin 임베딩을 fix
  - query 임베딩은 distillbert를 fine-tune해서 만들었음
  - in-batch negative 사용

## 유저 시퀀스 임베딩
### PinnerFormer: Sequence Modeling for User Representation at Pinterest 2022
- 기존 sequence 기반 추천 (SASRec, Bert4Rec)이 있지만 실시간 inference의 필요성이 생겼다.
- Transformer 모델이 next action prediction만이 아니라 긴 미래의 액션을 예측하게 학습
  - 실시간으로 하지 않고 배치 inference해도 되었다.
- 이전 PinnerSage와 다른점
  - 유저별 한 개의 벡터
  - 배치 inference
- 학습에 사용한 데이터
  - input
    - 저장, 클릭 등 1년치 sequence
    - positive, negative 액션 모두
  - label
    - positive 액션만 포함
  - source task
    - home feed 데이터만 포함
    - 다른 task(search, related pin)는 query라는 context가 있어서 제외
- 훈련
  - mixed batch negative
  - 1년치 input 중에 샘플링해서 샘플링 된 input당 1개씩 prediction
- 서빙
  - 하루 전날 pinterest 액션이 있던 유저만 추론 업데이트

## Retrieval
- 다양한 retrieval source 존재
- 특히 소셜미디어의 경우 룰 기반의 retrieval source 필요
  - ex) 팔로우 중인 보드
- graph 기반의 기술이 많이 사용
- 사이즈가 커서 좀 더 세분화 된 retrieval을 가지고 있다

### Pixie 2017
- graph 기반 retrieval
- pin, board를 bipartite graph로 만들어서 사용
- 특징
  - 실시간 inference
  - 150G RAM에 전체 그래프를 올릴 수 있음
  - 그래프 기반으로 굉장히 sparse한 경우에도 사용 가능

### Lightweight Ranking 2020
- 논문은 모르겠는데 pinterest engineering 블로그에 설명 존재
  - improving the quality of recommended pins with lightweight ranking
- candidate generation과 ranking의 중간
- XGBoost 사용
- 데이터
  - positive: action
  - negative: impressed(유저에게 노출되었으나 no action) + unimpressed(ranker에서 잘릴 경우)

### Two-tower 2021
- 논문은 모르겠는데 pinterest engineering 블로그에 설명 존재
  - pinterest home feed unified lightweight scoring a two tower approach

## Ranking
- 유저와의 상호작용이 많은 경우 multk-task를 고려할 수 있다
- ranking의 결과가 최종이 아니라 이를 기반으로 ordering하는 경우, 안정성과 설명가능성을 위해 calibration을 할 수 있다
- ranking에서 유저의 action sequence를 이용하고자 할 때 후보 아이템과 퓨전한 임베딩을 사용하는 경우 효과적

### Pinnability 2015
- pinnability machine learning in the home feed
- 수천개의 피처 사용
- LR, GBDT

### Multitask learning
- multi-task learning and calibration for utility based home feed ranking
- 다양한 action을 positive engagement로 묶고 weight를 줘서 loss에 사용
- calibration
  - down sampling correction
  - isotonic regression
  - plat scaling -> pinterest에서 사용

### AutoML
- how we use automl multi task learning and multi tower models for pinterest ads

### realtime user action, transformer