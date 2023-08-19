## 추천 데이터 특징

### user-item interaction data
- interaction data (feedback data)
  - 예들 들어, 영화에 대한 평점
  - regression or classification 
- explicit vs implicit
  - explicit은 수집이 어렵고 implicit은 선호도가 명확하지 않음 

### context data
- user의 시간, 공간, 네트워크 같은 데이터
  - 시간: 쇼핑몰에서 계절에 따라 옷 추천 등
  - 공간: 지역에 따라 선호하는 음식이 다를 수 있음 등
  - 네트워크: 유저의 친구들의 최근 관심사 등
- 해당 데이터를 이용해서 추천시스템을 만들 수 있다.
  - 사전 필터링: 사전에 context를 이용하여 필터링하고 ranking
  - 사후 필터링: 모델링 결과물을 context를 이용하여 필터링
  - context 모델링: 모델의 학습시 context data 이용

### 데이터 밀도
- sparse or dense?
  - sparse하면 당연히 정확한 추천 생성이 어렵다.
- sparsity 해결하는 방법
  - 결측치를 채운다.
  - 불균형의 경우 맞춰준다.
  - 모델을 이용하여 해결한다. (MF)

### 형태
- 범주형, 연속형, 시계열, 텍스트, 이미지, 오디오, 비디오

### 출처
- 온라인, 오프라인, 외부(기상데이터, 포털검색, 소셜미디어 등)
- 다양한 데이터를 섞어서 사용