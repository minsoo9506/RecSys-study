## 추천 시스템 구성 컴포넌트

### 로깅
- 로깅이 필요한 이유
  - 피드백 데이터 수집
  - AB test를 하기 위해
- 로깅의 종류
  - client side
    - 클라쪽에서 기록
    - 더 정확한 정보를 로깅
  - backend side
    - 서버에서 발생하는 이벤트 및 동작을 로그로 기록
    - 사용자의 요청, 알고리즘의 응답, 추천 결과 등을 포함
  - database side
    - 추천에 사용된 feature값을 로깅
    - 학습에 사용
    - feature값의 변화 감지

### feature transformer
- 다양한 데이터를 추천 모델 및 시스템이 사용할 수 있도록 변경
- ETL 발생
- Offline과 Online 환경에 따라 방법이 다르다.

### Retrieval을 위한 db
- ANN
  - SCaNN, FAISS
  - 한계점
    - 라이브러리라서 DBMS의 기능이 없다.
    - 검색엔진 기능이 없다.
- 검색엔진 데이터베이스
  - 검색 전용 비관계형 데이터베이스
  - full-text search, faceting
  - 검색과 추천을 동일한 인프라를 사용할 수 있다.
  - filter stage 기능 제공
  - db이기 때문에 id말고 필요한 데이터 필드를 가져올 수 있다.
  - 종류
    - ElasticSearch
      - 대표적인 검색엔진 데이터베이스
      - 최근에 knn, ann도 제공
    - Vespa

### feature store
- 목적
  - 모델에 이용할 feature를 빠르게 접근하기
  - offline, online에서 동일한 proessing을 유지하기
- 사용 db
  - 빠른 속도
  - key-value기반의 NoSQL을 많이 사용한다.

### 모델 추론 서버
- inference 할 수 있는 서버
- cpu로 시작한다.
- 모델 추론 라이브러리
  - BentoML
  - gRPC
    - http처럼 human readable은 아니고 protocol buffer를 사용

### 실험 플랫폼
- 실험플랫폼 없어도 AB test를 할 수 있다. 그런데 지속적인 테스트와 분석을 위해서라면 있으면 좋다.

## 구성 사례
- [spotify의 podcast 검색, vespa](https://engineering.atspotify.com/2022/03/introducing-natural-language-search-for-podcast-episodes/)
- 등등