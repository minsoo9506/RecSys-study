- personalized ranking
  - user에게 ranked list of items를 추천하는 것
- implicit feedback
  - 주로 positive feedback이다
  - non-observed item = real negative feedback + missing values

### Problem setting

- 전체 데이터를 pairwise perference $i >_u j$로 나타낸다.
- 각 user별로 item-item matrix를 만들고 implicit feedback을 통해서 어떤 item을 더 선호하는지 +, - 를 표시한다. 둘 다 feedback이 없는 경우는 빈칸으로 남긴다.
  - 따라서 학습셋 $D_s$ 은 positive, negetive, missing value로 이루어짐

### BPR

- bayesian 접근

$$p(\theta | >_u) \propto p(>_u|\theta)p(\theta)$$

$$\prod_{u \in U}p(>_u|\theta) = \prod_{(u,i,j) \in U\cdot I \cdot J}p(i>_uj|\theta)^{\delta((u,i,j)\in D_s)}(1-p(i>_uj|\theta))^{\delta((u,i,j)\in D_s)}\\=\prod_{(u,i,j)\in D_s}p(i >_u j | \theta)$$

- 따라서 $p(i >_u j | \theta)$를 어떤 모델를 통해 예측하면 된다.

$$p(i >_u j | \theta) = \sigma(\hat{x_{uij}(\theta)})$$

- 사전분포는 $p(\theta)\sim N(0, \Sigma_{\theta})$으로 한다.
- 이후에는 gradient descent로 optimization한다.
  - 데이터 전수가 아닌 bootstrap sampling해서 데이터를 사용한다.
