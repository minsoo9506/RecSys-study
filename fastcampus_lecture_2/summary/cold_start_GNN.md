- 이읏들의 정보를 이용해서 cold user를 다룬다. (gnn)
- knowledge graph를 이용할 수도 있다.

### 유저케이스: LINE의 GNN 활용 추천 (deview 2020)
- 1차적으로 MLP로 node 임베딩을 만들고 graph로 CTR prediction 진행
- 그러면 cold user/item이 발생했을때, 성능이 좋았다. (맨 처음에 아무것도 정보가 없는 상태는 아니라고 가정한듯)
- 결국 graph를 이용하면 edge가 많지 (interaction 정보) 않더라고 잘 추천할 수 있다는 의미같다.