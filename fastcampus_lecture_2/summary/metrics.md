# 정확도 지표
- 자세히 정리하지 않음

### MRR@K (Mean Reciprocal Rank)
- binary기반
- 각 유저마다 relevant item이 최초로 등장한 곳은 몇 번째인지 구하고 전체 유저의 mean값을 구한다.

### MAP (Mean Average Precision)
- binary기반
- 각 유저마다 relevant item이 등장할 때마다 precision을 구하고 평균을 내고 모든 유저의 average precision의 mean값을 구한다.

### NDCG

# 기타 지표

### Hit@K
- 유저에게 추천한 K개 중에 맘에 드는게 있었는지 계산한다.
- 있으면 1 없으면 0

### Diversity

### Novelty

### Serendipity
- 의도적으로 찾지 않았음에도 뭔가 새로운 좋은 것을 발견하는 경우를 의미한다.