## SSL
- label이 없거나 제한적으로 있을 경우 모델을 학습 시키는 방법
- 추천에서는 주로 SSL을 통한 Embedding 학습해서 사용한다. 

### Pseudo Label을 만드는 방법
- Generative method
  - 데이터의 일부분을 오염시키고 복원하는 것, bert에서 masking 방법 같은 것을 의미한다.
  - BERT4Rec에서 사용
- Constrastive method
  - 데이터를 다르게 Augmentation을 하고 모델에 넣어서 똑같이 만들 수 있도록 학습

### SSL을 한 뒤에
- joint training
  - SSL과 downstream task를 같이 학습
- pretrain and fine tuning

## 사례
### 네이버 플레이스: 나와 비슷한 음식점 취향을 가진 유저를 찾아주는 product
- input sequence 생성
- masking을 사용