- graph 알고리즘을 추천에 사용한 것
- bipartite 그래프를 GCN의 로직으로 link prediction해서 사용자에게 상품 추천

### Scalability Improvement
크게 3가지

- On-the-fly Convolution
  - node 주변 이웃을 샘플링해서 localized convolution을 적용, graphSAGE처럼
- Producer-consumer minibatch construction
  - cpu에서 '생산자'는 node 주변의 이웃을 추출한 뒤 convolution 연산을 위한 준비
  - gpu에서는 훈련을 수행
- Node Embedding via MapReduce
  - 맵리듀스 파이프라인을 통해 학습된 모델을 분산처리해서 빠르게 임베딩을 생성

### Training Technique
- 랜덤워크를 통한 컨볼루션 생성
  - 랜덤워크 기반 스코어링을 통한 중요 이웃 샘플링
- Importance Pooling
  - 랜덤워크 유사도 점수를 기반으로 Aggregation 과정에서 node feature에 가중치를 도입
- Curriculum Training
  - 학습과정에서 점점 더 어려운 예제를 학습하도록 유도하는 학습 도입
  - sample type:
    - high rank positive, low rank positive, high rank negative, low rank negative