## naive
### 인기 아이템 추천
### 랜덤 아이템 추천
- 다양한 아이템을 노출해서 exploration의 기능
- 하지만 relevance가 부족해서 유저가 이탈할 수 있음
### 인구 통계 기반 추천
- 나이, 성별, 지역 등의 정보로 인기 아이템 추천
### 규칙 기반 추천
- 서비스에서 얻은 도메인 지식을 활용해서 rule기반하여 추천

## preference elicitation (선호도 유도)
- 유저의 잠재된 선호를 이끌어 내는 방법들
- explicit, implicit한 방법 존재
### 온보딩 설문지
- 플랫폼에 처음 가입할 때 간단한 설문을 제시하여 정보 수집
### 아이템 선택, 순위 지정 유도
- 온보딩이랑 비슷
  -  예를 들어, 음악앱에서 처음 가입할 떄 선호하는 장르 선택하도록 유도
### 인터랙티브 퀴즈
- 대화형 인터페이스를 통해 고객의 선호 정보를 이끌어 내는 방법
### 소셜 미디어 연동
- 소셜 미디어 연동을 통해 친구들이 소비한 아이템을 추천해주는 방법
### 게임으로 만들기
- 게임의 구조처럼 유저가 자발적으로 정보를 채워 넣도록 유도
  - 예를 들어, Linkedin처럼 progress bar를 보여줘서 정보 채우도록 유도

## Feature 정보 활용
- cold start 문제도 결국 모델링/서빙 시점에서 data sparsity라고 생각할 수 있다.
### point-wise prediction
- user, item의 feature를 만들어서 (concat) 모델훈련을 하고 prediction해서 cold-user에 대해 추천한다.
### 비지니스 케이스
- 중고차량 추천 문제 (by Mobile.de)
  - user, item feature를 구하고 딥러닝 모델을 통해 분류 진행
  - 이 과정으로 임베딩을 만들어서 Nearest neighbor 같은 로직으로 candidate generation