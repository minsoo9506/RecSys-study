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
  - 개인화되 추천
  - 실제 facebook 추천시스템에 적용