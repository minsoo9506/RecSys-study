# 추천의 설명가능성
### Explore, Exploit and Explain: Personalizing Explainable Recommendations with Bandits 2018년
- feedback loop를 개고 다양한 추천, 좋은 설명을 제공
- 홈피드 추천
- Bart (bandits fo recommendations as treatments)
  - candidate set이 정해진 상태에서 추천
  - reward를 예측(ranking)하는데 어떤 모델을 사용했는가
    - FM사용
  - 어떻게 MAB로 홈페이지를 만들었는가
    - 위아래, 좌우 스크롤 모두에 사용
  - Bandit의 결과를 어떻게 모델학습에 사용했는가
    - counterfactual risk minimization

## 플레이 리스트
### Humans + Machines: A Look Behind the playlists powered by spotify's algotorial technology 2017년
- Algotorial = altorithm + editorial
1. 특정 사용자 요규 사항 구상
2. 내용에 대한 가설 설정 (예, 자동차여행시 들으면 좋은 노래)
3. 에디터가 적합한 노래를 구성하여 pool 생성 (candidate generation)
4. 알고리즘이 그 pool에서 적합한 개인화 플레이리스트 생성 (ranking)
5. 플레이리스트에 적합한 다양한 커버 디자인 제작
6. 알고리즘이 개인화하여 커버 이미지 선택