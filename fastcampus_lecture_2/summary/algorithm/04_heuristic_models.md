## Utility Score 기반 추천
- 휴리스틱한 함수를 통해서 score를 만드는 것이다.
- 베이스라인으로 사용하기 좋다.

## 사례

### youtune candidate generation
- 2010년 논문
- seed가 들어오면 관련있는 비디오 뽑기
- 24시간동안 두 비디오가 모두 시청된 횟수를 count해서 두 비디오의 관련성을 측정했다.
- TF-IDF를 사용하기도 했다.

### SWIGGY
- 인도 음식 배달앱 기업
- Evolution of and Experiments with Feed Ranking at SWIGGY, 2019
  - 먼저 utility score로 시작하고 GBDT로 전환했다고 한다.
- 3가지로 구성 (간단한 룰베이스)
  - customer preference score
  - restaurant similarity score
    - LDA (topic modeling)
  - restaurant popularity score

### Musinsa
- 검색어 분석을 통한 상품 정렬 개선, 2021년