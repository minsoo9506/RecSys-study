- 추천시스템 공부
  - Date: 2022.09 ~
  - 기본개념, 모델구현, 논문리딩, 프로젝트

# Study Materials

<details>
<summary>패스트캠퍼스 딥러닝을 활용한 추천시스템 구현 올인원 패키지 Online `ing`</summary>
<div markdown="1">

- data
  - MovieLens(small)
  - KMRD(small)
  - Netflix
- 이론 (summary)
  - [content-based filtering](./fastcampus_lecture/summary/contents_based_filtering.md)
  - [neighborhood-based collaborative filtering](./fastcampus_lecture/summary/neighborhood_based_collaborative_filtering.md)
  - [model-based filtering](./fastcampus_lecture/summary/model_based_filtering.md)
  - [hybrid recommender system](./fastcampus_lecture/summary/hybrid_recommender_system.md)
  - [contextual aware recommender system](./fastcampus_lecture/summary/contextual_aware_recommender_system.md)
  - [evaluation metric](./fastcampus_lecture/summary/evaluation_metric.md)
- 실습 (code)
  - [movielens EDA](./fastcampus_lecture/notebook/00_movielens_eda.ipynb)
  - [movielens simple model](./fastcampus_lecture/notebook/01_movielens_simple_model.ipynb)
  - [movielens content-based filtering: TFIDF](./fastcampus_lecture/notebook/02_movielens_contents_based_filtering_TFIDF.ipynb)
  - [movielens neighborhood-based collaborative filtering](./fastcampus_lecture/notebook/03_movielens_neighborhood_based_collaborative_filtering.ipynb)
  - [movielens matrix factorization: svd](./fastcampus_lecture/notebook/04_movielens_matrix_factorization_svd.ipynb)
  - [KMRD, Netflix EDA](./fastcampus_lecture/notebook/05_KMRD_netflix_eda.ipynb)

</div>
</details>

# Code

- pytorch, pytorch_lightning

### Algorithm

|             Model              |                     Model Code                      |                           Example Code                           |
| :----------------------------: | :-------------------------------------------------: | :--------------------------------------------------------------: |
| Matrix Factorization with SGD  |            [`model`](./src/model/MF.py)             | [`movielens example`](./notebook/example_MF_SGD_movielens.ipynb) |
| Neural Collaborative Filtering | [`model`](./src/model/NCF.py), `lit_model`, `train` |                           KMRD example                           |

# Paper Read

### Algorithm

- Collaborative Filtering for Implicit Feedback Data, 2008 [`review`](./paper_review/Collaborative%20Filtering%20for%20Implicit%20Feedback%20Data.md)
- BPR: Bayesian Personalized Ranking from Implicit Feedback, UAI 2009 [`review`](./paper_review/BPR%3A%20Bayesian%20Personalized%20Ranking%20from%20Implicit%20Feedback.md)
- Context-Aware Recommender Systems, 2011
- Neural Collborative Filtering, 2017 IWWWC [`review`](./paper_review/Neural%20Collaborative%20Filtering.md)

### Diversity

- Algorithmic Effects on the Diversity of Consumption on Spotify, WWW 2020

# Other Sources

### Use Case

- 카카오 AI 추천: 카카오페이지와 멜론으로 살펴보는 카카오 연관 추천
- 카카오 AI 추천: 토픽모델링과 MAB를 이용한 카카오 개인화 추천
- 카카오 AI 추천: 협업필터링 모델 선택 시의 기준에 대하여
- 카카오 AI 추천: 카카오의 콘텐츠 기반 필터링
- 우리 생활 속 추천 시스템, 어떻게 발전해왔고, 어떻게 발전해나가고 있는가? (카카오 김성진 팀장, 2021.12)
- 추천 기술이 마주하고 있는 현실적인 문제들 (카카오 김성진 리더, 2021.10)
- if(kakao)2019 멜론 플레이리스트 자동 생성
- if(kakao)2020 맥락과 취향 사이 줄타기
- 브런치 추천의 힘에 대한 6가지 기술
- 딥러닝 개인화 추천 (당근마켓, 2019)
- 번개장터 추천시스템 개발 및 도입후기 (2017)
- 비용 효율적인 Click-Through Rate Prediction 모델로 하쿠나 라이브 추천시스템 구축하기
- LINE Timeline의 새로운 도전 (2020.04)
- (Deview2021) BERT로 만든 네이버 플레이스 비슷한 취향 유저 추천 시스템
- (Deview2021) Knowledge Graph에게 맛집과 사용자를 묻는다: GNN으로 맛집 취향 저격 하기
- (Deview2020) 유저가 좋은 작품(웹툰)을 만났을 때
- (Deview2020) 추천시스템 3.0: 딥러닝 후기시대에서 바이어스, 그래프, 그리고 인과관계의 중요성
- NDC21-데이터분석, 추천알고리즘 offline A/B 테스트 (feat: PAIGE 프로야구 서비스)
