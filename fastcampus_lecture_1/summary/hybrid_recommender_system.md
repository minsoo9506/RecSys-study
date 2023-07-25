- 여러가지의 추천알고리즘을 사용하는 것

# 종류

|                     |                                      설명                                      |
| :-----------------: | :----------------------------------------------------------------------------: |
|  Weighted Ensemble  |           여러 모델의 추천 결과를 ensemble하여 최종 추천아이템 선정            |
|        Mixed        |                          여러 모델의 결과를 같이 사용                          |
|       Switch        |        사용자, 서비스의 상태에 따라 여러 추천 알고리즘을 그 때마다 선택        |
| Feature Combination |            다양한 feature를 조합하여 추천 알고리즘을 학습하고 추천             |
|     Meta-Level      | 특정 모델의 결과가 다시 다른 모델의 input이 되면서 서로의 결과를 학습해서 추천 |