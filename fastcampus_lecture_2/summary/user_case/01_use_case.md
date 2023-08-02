# eBay
## 비슷한 상품 추천
- iterm-based collaborative filtering을 사용 2010년
### optimizing similar item recommendations in a semi-structured marketplace to maximize conversion 2016년
- retrieval
  - 아이템의 상위 카테고리가 있다면 동일한 카테고리의 다른 아이템 추천
  - 같은 세션에서 같이 자주 본 아이템 & 동일 카테고리 필터
  - title similarity (elasticsearch)
- ranking
  - 구매로그를 이용한 binary classification
  - non-clicked vs purchased
  - negative sampling
  - logistic regression 사용

## 같이 살 상품 추천
## complementary item recommendations at eBay Scale 2019년
- collaborative filtering을 사용하기 어려운 이유
  - 비슷한 상품 추천이 되기 쉽다.
- 그래서 같이 살 상품을 추천하기 위해 category filter를 만들었다.
  - 먼저 item을 그룹화한다. (category화)
  - user-category matrix로 계산하고 seed item 카테고리와 유사한 카테고리를 구한다.
- retrieval
  - 사용하는 retrieval: 연관된 상품, co-views, 관련된 쿼리&검색, DeepRecs
  - 필터: 카테고리 필터, 호환성 필터
- 아키텍쳐
  - spark를 활용한 offline computation
  - gpu를 이용한 KNN search offline calculation
  - KNN 결과를 key-value store에 저장
- ranking
  - binary classfication으로 비슷한 상품 추천과 유사
- 특징
  - 단순한 MF는 production에서 사용하기 어렵다.
  - 대체제가 아닌 보완제를 위한 추천은 카테고리 필터가 유용하다.
  - 데이터가 너무 sparse할 때는 묶어서 이용할 수 있다.
  - MF를 이용해 카테고리 유사도를 구할 수도 있다.
  - offline computation을 기반으로도 큰 스케일의 추천 시스템을 만들 수 있다.

## 개인화 추천
- 유저, 유저와 아이템의 상호작용 데이터
### personalized embedding-based e-commerce recommendations at eBay 2021년
- 유저임베딩: 최근 유저의 액션에 해당하는 아이템 임테딩을 sequential하게 녹여서 유저임베딩을 만들었다.
- 아이템임베딩: 아이템 제목, 메타, 카테고리들의 임베딩들을 MLP layer에 태워서 만들었다.
  - 둘 다 id정보는 없다.
  - 새로운 유저, 아이템이 와도 결과를 바로 계산할 수 있다. (물론 첫 로그인 유저의 경우는 로그가 어느정도 쌓여야 하겠지만)
- 두 임베딩 dot product해서 loss 계산해서 업데이트를 진행한다.
- 노출되었지만 click하지 않은 데이터를 negetive로 학습하면 generalization이 부족할 수도 있다.
  - 예를 들어, 특정 페이지에 청바지1, 청바지2, 청바지3이 노출되고 2,3이 negetive가 되면 청바지에만 overfitting될 수 있는 것이다.
  - 그래서 in-batch negative 방법이 효과적일 수 있는 것이다. (특히, retrieval단계에서)
### building a deep learning based retrieval system for personalized recommendations 2022년
- 처음에는 offline
  - 아이템, 유저 임베딩을 모두 offline으로 만들고 KNN도 offline으로 진행
  - 그래서 유저 request가 오면 바로 key-value로 저장된 값을 가져가서 보여준다.
- offline/NRT hybrid
  - KNN은 online
  - 큰 차이는 없을 수 있다. 이미 임베딩은 offline으로 만들어져 있으니까 그렇다.
- NRT
  - 유저임베딩, KNN은 online
  - 유저 input이 들어오면 실시간으로 유저임베딩벡터가 업데이트되고 이를 KNN으로 아이템을 찾는다.

## 비슷한 상품 추천 ranking
### multi-relevance ranking model for similar item recommendation 2022년
- 단계
  - retrieval -> ranking -> ordering(광고)
- GBDT로 ranking을 사용했다.
- feature를 만드는게 핵심이었다.
  - user-item historical data
  - item-item title similarity
  - user data
  - context
- 기존에는 binary(구매) label을 사용했다.
  - 하지만 한계점이 있다.
  - 구매로 이어지지 않아도 좋은 추천일 수도 있다.
  - 클릭과 같은 액션에 비해 sparse하다. (장바구니, 위시리스트 추가 등의 액션도 있음)
- 그래서 action을 relevance 레벨을 정했다고 한다. (구매일수록 강한 것)
- 이를 기반으로 BDT에서 pairwise loss function을 사용(action label끼리 pairwise하게) -> label마다 weight 가능

### how eBay created a language model with three billion item titles 2023년
- item-item title 유사도를 위해 bert를 도입했다.
- bert는 domain-specific하지 않고 무겁다.
- bert를 fine-tuning해서 eBERT를 만들고 -> knowledge distillation을 해서 경량화 -> siamese network (metric learning, two-tower와 유사)

## 이커머스 추천 시스템의 특징
- 연관성의 정의 조심
  - 비슷한 상품? 같이 산 상품?
- 이커머스의 경우 아이템의 메타테이터가 부정확, 부족한 경우가 많다.
  - 다양한 retrieval로 보완
- 텍스트 기반의 컨텐츠 데이터가 중요
- 유저의 목표가 상대적으로 명확하다.