### MF (Matrix Factorization)
- 행렬 추론: offline, batch
- 새로운 유저, 아이템이 포함 x
- 새로운 유저, 아이템을 고려할 경우 재학습 필요
- cold start, sparsity 문제, 유저*아이템 interaction이외의 다른 정보를 사용못함

이후 side information feature를 사용할 수 있는 모델들이 나왔다.

### Linear Model
- 다양한 feature를 만들어서 logistic regression으로 CTR 예측해서 추천

### FM (Factorization Machines)
- linear한 feature와 feature끼리의 interaction도 고려

### FFM (Field-aware Factorization Machines)

이제 더 딥러닝을 딥하게 사용하고 회사들이 사용하는 경우를 알아보자.

- industry에서 추천 모델은 크게 2가지로 나누어서 생각할 수 있다.
  - candidate generation
  - ranking

### Classic deep neural network
- Deep Crossing
- Youtube DNN
  - candidate generation과 ranking으로 나눠짐
  - ANN(approximate nearest neighbot)을 사용한 candidate generatioin

### Replace CF with NN
- NeuralCF
  - MF에서 dot product하는 부분을 nn으로 바꿈
  - 여전히 side information을 못씀
- Two-tower
  - side information 사용가능
  - 여러 회사들이 candidate generation에 사용

### Shallow and deep model
- Wide & Deep
  - continuous feature는 그대로, categorical feature는 임베딩
  - categorical feature끼리 cross product 진행
- DeepFM
  - Wide & Deep의 변형
  - Wide부분을 FM으로 대체
  - cross feature를 위한 feature engineering이 불필요
  - categorical feature들이 같은 크기의 임베딩 사이즈를 가짐

### Apply attention mechanism (nlp)
- Bert4Rec

### GNN, Knowledge graph
- social network 업계에서 주로 사용
- side information을 사용 못하는 경우가 많아 candidate generation에 주로 사용