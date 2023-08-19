- 추천시스템 공부
  - 기본개념, 모델구현 및 대회참여, 논문리딩, 프로젝트

<h3>:open_book: Index</h3>
<!-- TOC -->

- [Study](#study)
- [Practice](#practice)
- [Project](#project)
- [Paper Read](#paper-read)
    - [Algorithm](#algorithm)
    - [Algorithm - text, image](#algorithm---text-image)
    - [Algorithm - session-based, sequential](#algorithm---session-based-sequential)
    - [Algorithm - graph](#algorithm---graph)
    - [Diversity](#diversity)
    - [Bias](#bias)
    - [User Modeling](#user-modeling)
    - [Causality](#causality)
    - [Survey](#survey)
- [Other Resources](#other-resources)
    - [Industry](#industry)
    - [others](#others)

<!-- /TOC -->

# Study

<details>
<summary>패스트캠퍼스 강의1</summary>

- data
  - MovieLens(small)
  - KMRD(small)
  - Netflix
- 이론 (summary)
  - [content-based filtering](./fastcampus_lecture_1/summary/contents_based_filtering.md)
  - [neighborhood-based collaborative filtering](./fastcampus_lecture_1/summary/neighborhood_based_collaborative_filtering.md)
  - [model-based filtering](./fastcampus_lecture_1/summary/model_based_filtering.md)
  - [hybrid recommender system](./fastcampus_lecture_1/summary/hybrid_recommender_system.md)
  - [contextual aware recommender system](./fastcampus_lecture_1/summary/contextual_aware_recommender_system.md)
  - [evaluation metric](./fastcampus_lecture_1/summary/evaluation_metric.md)
- 실습 (code)
  - [movielens EDA](./fastcampus_lecture_1/notebook/00_movielens_eda.ipynb)
  - [movielens simple model](./fastcampus_lecture_1/notebook/01_movielens_simple_model.ipynb)
  - [movielens content-based filtering: TFIDF](./fastcampus_lecture_1/notebook/02_movielens_contents_based_filtering_TFIDF.ipynb)
  - [movielens neighborhood-based collaborative filtering](./fastcampus_lecture_1/notebook/03_movielens_neighborhood_based_collaborative_filtering.ipynb)
  - [movielens matrix factorization: svd](./fastcampus_lecture_1/notebook/04_movielens_matrix_factorization_svd.ipynb)
  - [KMRD, Netflix EDA](./fastcampus_lecture_1/notebook/05_KMRD_netflix_eda.ipynb)

</details>

<details>
<summary>패스트캠퍼스 강의2</summary>

- 이론 (summary)
  - [use case](./fastcampus_lecture_2/summary/use_case/)
    - eBay, Doordash, Spotify, Pinterest
  - [cold start](./fastcampus_lecture_2/summary/cold_start/)
  - [algorithm](./fastcampus_lecture_2/summary/algorithm/)
  - [RecSys architecture](./fastcampus_lecture_2/summary/recsys_architecture/)
  - [data and algorithm](./fastcampus_lecture_2/summary/data_and_algorithm/)
    - 데이터 종류
    - 비정형 데이터 분석 방법론
    - 데이터별 알고리즘 적용 및 결과분석

</details>

# Practice

- LG Uplus 추천 대회 참여 [`repository`](https://github.com/minsoo9506/lg-uplus-RecSys-competition)
- Kaggle OTTO 따라잡기 [`folder`](./kaggle_OTTO/)

# Project
- 모델 구현 [`repository`](https://github.com/minsoo9506/RecModel)

# Paper Read

### Algorithm

- Collaborative Filtering for Implicit Feedback Data, 2008 [`review`](./paper_review/Collaborative%20Filtering%20for%20Implicit%20Feedback%20Data.md)
- BPR: Bayesian Personalized Ranking from Implicit Feedback, UAI 2009 [`review`](./paper_review/BPR%3A%20Bayesian%20Personalized%20Ranking%20from%20Implicit%20Feedback.md)
- Context-Aware Recommender Systems, 2011
- Neural Collaborative Filtering, 2017 IWWWC [`review`](./paper_review/Neural%20Collaborative%20Filtering.md)
- Fatorization Machines, 2009 [`review`](./paper_review/Factorization%20Machines.md)
- Wide & Deep Learning for Recommender Systems, 2016 [`review`](./paper_review/Wide%20%26%20Deep%20Learning%20for%20Recommender%20Systems.md)
- DeepFM: A Factorization-Machine based Neural Network for CTR Prediction, 2017 [`review`](./paper_review/DeepFM%3A%20A%20Factorization-Machine%20based%20Neural%20Network%20for%20CTR%20Prediction.md)
- AutoRec: Autoencoders Meet Collaborative Filtering, 2015 WWW
- Training Deep AutoEncoders for Collaborative Filtering, 2017 [`review`](./paper_review/Training%20Deep%20AutoEncoders%20for%20Collaborative%20Filtering.md)
- Variational Autoencoders for Collaborative Filtering, 2018
- Deep content-based music recommendation, 2013 NIPS
- Deep Learning Recommendation Model for Personalization and Recommendation Systems (DLRM), 2019 [`paper`](https://arxiv.org/pdf/1906.00091.pdf)
- DCN V2: Improved Deep & Cross Network and Practical Lessons for Web-scale Learning to Rank Systems 2020 [`paper`](https://arxiv.org/pdf/2008.13535.pdf)

### Algorithm - text, image
- Joint Training of Ratings and Reviews with Recurrent Recommender Nerworks, 2017 ICLR [`review`](./paper_review/Joint%20Training%20of%20Ratings%20and%20Reviews%20with%20Recurrent%20Recommender%20Nerworks.md)
- Image-based Recommendations on Styles and Substitutes, 2015 SIGIR
- VBPR: Visual Bayesian Personalized Ranking from Implicit Feedback, 2016 AAAI
- Deep Neural Networks for YouTube Recommendations, 2016 RecSys [`paper`](https://static.googleusercontent.com/media/research.google.com/ko//pubs/archive/45530.pdf)
- Recommending What Video to Watch Next: A Multitask Ranking System, 2019 RecSys

### Algorithm - session-based, sequential

- Session-based Recommendations with Recurrent Neural Networks, 2015 ICLR
- BERT4Rec: Sequential Recommendation with Bidirectional Encoder Representations from Transformer, 2019 [`paper`](https://arxiv.org/abs/1904.06690)
- SASRec: Self-Attentive Sequential Recommendation, 2018 [`paper`](https://arxiv.org/abs/1808.09781)

### Algorithm - graph
- PageRank: Standing on the shoulders of giant, 2010 [`paper`](https://arxiv.org/pdf/1002.2858.pdf)
- DeepWalk: Online Learning of Social Representations, 2014 [`paper`](https://arxiv.org/pdf/1403.6652.pdf)
- SEMI-SUPERVISED CLASSIFICATION WITH GRAPH CONVOLUTIONAL NETWORKS, 2017 [`paper`](https://arxiv.org/pdf/1609.02907.pdf)
- Inductive Representation Learning on Large Graphs, 2017 [`paper`](https://arxiv.org/pdf/1706.02216.pdf)
- Graph Attention Networks, 2018 [`paper`](https://arxiv.org/pdf/1710.10903.pdf)
- Graph Convolutional Neural Networks for Web-Scale Recommender Systems [`paper`](https://arxiv.org/pdf/1806.01973.pdf)

### Diversity
- Algorithmic Effects on the Diversity of Consumption on Spotify, WWW 2020

### Bias
- Lessons Learned Addressing Dataset Bias in Model-Based Candidate Generation at Twitter, 2020 KDD IRS [`review`](./paper_review/Lessons%20Learned%20Addressing%20Dataset%20Bias%20in%20Model-Based%20Candidate%20Generation%20at%20Twitter.md)
- Popularity-Opportunity Bias in Collaborative Filtering, WSDM 2021 [`paper`](https://dl.acm.org/doi/pdf/10.1145/3437963.3441820) [`review`](./review/Popularity-Opportunity%20Bias%20in%20Collaborative%20Filtering.md)

### User Modeling
- Exploring the longitudinal effects of nudging on users’ music
genre exploration behavior and listening preferences, 2022 [`paper`](https://dl.acm.org/doi/pdf/10.1145/3523227.3546772)
- Personalizing Benefits Allocation Without Spending Money: Utilizing Uplift Modeling in a Budget Constrained Setup, Recsys2022 [`video`](https://dl.acm.org/doi/10.1145/3523227.3547381)

### Causality
- Inferring the Causal Impact of New Track Releases on Music Recommendation Platforms through Counterfactual Predictions, RecSys2020 [`papers`](https://labtomarket.files.wordpress.com/2020/08/recsys2020lbr.pdf?utm_source=LinkedIn&utm_medium=post&utm_campaign=monday_posting&utm_term=2023_07_24)

### Survey
- Deep Learning based Recommender System: A Survey and New Perspectives, 2019

# Other Resources
### Industry
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
- 데이터야놀자2022, 뭐먹지 빌런을 무찌르는 GNN 기반 개인화 추천 - 윤기태님 [`review`](./review/%EB%AD%90%EB%A8%B9%EC%A7%80%20%EB%B9%8C%EB%9F%B0%EC%9D%84%20%EB%AC%B4%EC%B0%8C%EB%A5%B4%EB%8A%94%20GNN%20%EA%B8%B0%EB%B0%98%20%EA%B0%9C%EC%9D%B8%ED%99%94%20%EC%B6%94%EC%B2%9C.md)
- if(kakao)dev2022 Sequential Recommendation System 카카오 서비스 적용기
- if(kakao)dev2022 Explainable Recommender System in 카카오웹툰
- [무신사가 카테고리숍 추천을 하는 방법](https://medium.com/musinsa-tech/%EB%AC%B4%EC%8B%A0%EC%82%AC%EA%B0%80-%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%EC%88%8D-%EC%B6%94%EC%B2%9C%EC%9D%84-%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95-a45b219685ea)
- [검색어 분석을 통한 상품 정렬 개선, 무신사 2021](https://medium.com/musinsa-tech/%EA%B2%80%EC%83%89%EC%96%B4-%EB%B6%84%EC%84%9D%EC%9D%84-%ED%86%B5%ED%95%9C-%EC%83%81%ED%92%88-%EC%A0%95%EB%A0%AC-%EA%B0%9C%EC%84%A0-b92ded2923c3)
- [Introducing Natural Language Search for Podcast Episodes, spotify 2022](https://engineering.atspotify.com/2022/03/introducing-natural-language-search-for-podcast-episodes/)
- [Modeling Users According to Their Slow and Fast-Moving Interests, spotify 2022](https://research.atspotify.com/2022/02/modeling-users-according-to-their-slow-and-fast-moving-interests/)
- [Building a Deep Learning Based Retrieval System for Personalized Recommendations,ebay 2022](https://tech.ebayinc.com/engineering/building-a-deep-learning-based-retrieval-system-for-personalized-recommendations/)

### others
- Transformers4Rec: A flexible library for Sequential and Session-based recommendation
- [[22'Recsys] BERT4Rec 구현의 진실에 관하여 : A Systematic Review and Replicability Study of BERT4Rec for Sequential Recommendation](https://mytype9591.tistory.com/m/6)
- [Recommender Systems, Not Just Recommender Models, nividia merlin](https://medium.com/nvidia-merlin/recommender-systems-not-just-recommender-models-485c161c755e)
- [Scaling deep retrieval with TensorFlow Recommenders and Vertex AI Matching Engine](https://cloud.google.com/blog/products/ai-machine-learning/scaling-deep-retrieval-tensorflow-two-towers-architecture?hl=en)
- [DLRM github](https://github.com/facebookresearch/dlrm)
- [DeepCTR github](https://github.com/shenweichen/DeepCTR)
