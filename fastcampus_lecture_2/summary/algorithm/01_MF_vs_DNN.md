### MF
- 미리 임베딩을 구해놓을 수 있다.
- ANN이 가능하다.
- cold start에 약하다. 새로 데이터를 추가하려면 모든 데이터에 대해 재학습이 필요하기 떼문이다.

### softmax DNN
- DNN을 이용하여 유저임베딩을 구하고 마지막 layer에 아이템임베딩과의 dot product를 통해서 muliclass classfication하는 모델을 의미한다.
  - 주로 아이템임베딩은 따로 만든다고 가정한다.
- ANN이 가능하다.
- cold start에 대한 재학습의 필요성이 적다. MF보다 더 많은 정보를 feature로 넣을 수 있기 때문이다.
- 유저의 상태가 바뀌어도 재학습을 하지 않더라도 추론을 통해서 달라진 prediction을 만들 수 있다.
- multiclass가 너무 많기 때문에 negetive sampling등의 기술을 적용해야한다.