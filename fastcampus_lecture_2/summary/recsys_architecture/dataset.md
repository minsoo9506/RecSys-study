### CF 기반의 추천 시스템 데이터
- Explicit Feedback data
  - 예: 좋아요, 별점
  - 유저의 강한 의지, 조작의 가능성 존재
- Implicit Feedback data
  - 예: 클릭, 장바구니, 시청시간
  - 데이터의 양이 많다, negative라고 확실히 단정짓기 어렵다 

## 데이터셋 생성
### Label 생성하기
- 주로 implicit feedback을 사용한다.
- 그렇다면 negative는 어떻게 정할지 고민해야한다.

### Continuous Feedback
- continuous feeedback 데이터는 count, avg 등의 aggregation 결과를 feature 사용한다.
1. 유저 퍼널을 통해 중요한 action 생각하기
2. 이를 토대로 entity 추출하기 (예: 고객, 지역, 상품 등등)
3. entiry를 grouping 하기 (예: 유저: 나이, 성별, 지역)
4. 기간을 설정
5. 이제 agg 함수를 선택해서 feature 생성 (예: 유저가 일주일 시청한 영화 장르 클릭 count)
6. feature를 너무 크지 않도록 하고 너무 sparse한 것도 조심

### Categorical data
- 대부분 sparse해서 dense한 임베딩으로 바꾸려고 하는 경우가 많다.
- 많은 경우 다른 task에서 미리 임베딩을 생성해서 사용한다.

### Content 데이터 생성하기
- 자신들의 서비스를 잘 살펴봐야한다.

### Query, Context, Item 데이터 구분하기
- Query, Context
  - 주로 request 한 번당 한 개를 가져온다.
  - 자주 바뀌는 값이다.
- Item
  - request 한 번당 여러 개를 가져와야 한다.
  - 상대적으로 적게 바뀌는 편이다.

### Online, Offline 데이터 구분하기
- Offline
  - context, metadata, categorical data, 긴 시간의 피드백 데이터
- Online
  - 짧은 기간의 피드백, context가 담겨있는 데이터
  - 주로 ranking단계에서 많이 사용