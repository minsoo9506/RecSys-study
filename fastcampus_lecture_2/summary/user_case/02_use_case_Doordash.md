# DoorDash
- 음식 배달 도메인
## 머신러닝 기반 추천
### Powering Search & Recommendations at DoorDash (2017년)
- 어려운 점 -> 아래와 같은 이유로 일반적인 collaborative filtering은 사용하기 어려움
  - 온라인 서비스지만 오프라인 제약
  - cold start 문제
  - 상대적으로 다양성이 중요
  - 배달 거리 중요
- retrieval은 복잡하지 않고 geohash로 locality를 고려해서 진행
- ranking은 구매여부를 logistic regression으로 분류문제로 진행
  - feature에 유저 feature가 있고 online으로 유저 정보를 사용

### Personalized Store Feed with vector embeddings 2018년
- store2vec
  - vocab은 가게, setence는 유저가 세션동안 클릭한 가게
  - 유저 임베딩은 지난 6개월간 주문 or 최근 100개 주문한 가게의 임베딩 합
  - 유저와 가게 거리는 cosine similarity
- 한계
  - cold start

### Integration a searc ranking model into a prediction service 2020년
- 엔지니어링 관련 내용

## 딥러닝 기반 추천
### Using triploet loss and Siamese Neural networks to train catalog item embeddings 2021년
- 유저: 유저가 구매한 음식, 식당: 식당이 파는 음식
- 왜 word2vec을 사용하지 않은 이유?
  - 새로운 아이템이 들어오면 항상 재학습에 필요
  - 굉장히 sparse하다
- 왜 supervised learning을 통한 임베딩을 이용하지 않았나?
  - 임베딩이 반드시 metric의 특징을 가지리라는 보장이 없다.
  - 좋은 label을 얻기 어렵다.
  - + bert는 느린 인퍼런스, 데이터가 많으면 pretrain이 없어도 성능이 잘 나옴
- item id가 아닌 텍스트 자체를 토큰화해서(trigram) 인풋으로 사용
  - 새로운 음식이 들어와도 추론 가능 (cold start에 유리하다)
  - 쿼리 역시 추론 가능
- label
  - 같은 세션에서 같이 검색하고 구매한 경우 연관있는 positive라고 함
  - negative는 텍스트의 거리가 먼 것들
- Triplet loss
  - positive관계의 임베딩은 가깝게 negative관계의 임베딩끼리는 멀게 만드는 loss

## 딥러닝을 이용한 홈페이지 추천
### Leveraging the pipeline design pattern to modularize recommendation services 2021년

### Homepage recommendation with exploitation and Exploration 2022년
- universal ranker: 딥러닝 기반 ranking 모델
- uncertainty model: UCB 기반
  - 노출이 많이 될수록 uncertainty가 줄어듬

## MAB 기반 추천
- MAB 사용
  - 랭킹결과에 exploration 추가
  - AB테스트 대신 MAB로 테스팅
  - candidate 수가 적을 때 추천 자체를 MAB로 진행 (배너, 대표이미지, 카테고리 순서)
- 특징
  - UI를 개인화 할 떄 MAB를 사용할 수 있다.
  - 다양한 사전정보를 활용하여 유용한 MAB를 만들 수 있다.
  - 실제 production에서는 수학적으로 엄밀하지 않더라고 유용하게 사용할 수 있다.

### Personalized Cuisine Filter 2020년
- Multi-level MAB를 이용하여 개인화 + 로컬카테고리
  - 지역을 계층적으로 나눈것이 multi-level
  - Bernoulli Thompson Sampling MAB 사용
- multi-level을 사용한 이유
  - 사전 구매 정보가 없는 고객에게도 지역을 기반 사전지식으로 추천이 가능
  - 지역의 인기도를 반영하여 추천

### Selecting the Best Image for Each Merchant Using Exploration and Machine Learning 2023년
- 가게의 이미지를 어떻게 정할까?
- 첫번쨰 시도: 룰베이스 필터
  - 사이드, 음료가 아니여야 한다.
  - AB테스트 결과 conversion 상승
- 두번쨰 시도: 이미지 로테이션
  - 대표이미지 + 가장 많이 팔린 음식 사진 3개
  - AB테스트 결과 click증가, conversion 감소
  - 따라서, 높은 퀄리티에 구매 가능성이 높은 사진을 뽑아야 한다.
- 세번째 시도: MAB
  - 사용이유
    - 고객들의 취향이 바뀔수도 있다.
    - 더 좋은 이미지가 생길 수도 있다.