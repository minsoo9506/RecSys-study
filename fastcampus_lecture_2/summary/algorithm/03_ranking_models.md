## ranking 알고리즘
- binary classification을 주로 진행한다.
- 이 과정에서 advanced하게 진행되는 부분들을 나누면 multi-modal, multi-task, cross-feature로 나눌 수 있다.
  - 실제로 구글, 인스타그램 등에서 실제 서빙 관련 논문도 발표했다.

### GBDT
- 예시
  - 네이버 검색 2022년, 하이퍼커넥트 라이브 추천 2021년

### DLRM
- 특징
  - 2019년 meta에서 오프소스로 공개한 Deep Learning Ranking Model
  - 대규모 데이터 처리 (하드웨어적인 내용이 많음ㅠ)
  - 사용자와 아이템 특징 벡터
  - 상호작용 모델링
  - 개인화된 추천
  - 실제 facebook 추천시스템에 적용

### DCN v2
- Deep & Cross Network
- 구글의 광고 추천 분야에서 사용
- 장점
  - FE없이 자동으로 중요한 feature cross를 찾아준다. cross layer를 이용해 효율적으로 feature cross 계산이 가능하다.
  - categorical feature의 vocab size에 따라 embedding size를 선택할 수 있다.
  - second order보다 더 높은 차원도 가능하다.
  - performance와 모델크기 간의 tradeoff 방법을 제시했다.