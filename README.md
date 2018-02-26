# Machine-Learning-Tutorial
### *WARNING, this README got heavy GIF files to load.*

Code Machine learning models from scratch. Trying to implement some optimizers and models from scratch. Will try to update over time.

1. [Evolution Strategies Optimizer](deep-evolution-entropy)
2. [Deep feed-forward on (Gradient Descent, Momentum Gradient Descent, Nesterov Momentum, Adagrad, RMSprop, ADAM)](deep-feed-forward)
3. [Vanilla Recurrent Neural Network on (Gradient Descent, Momentum Gradient Descent, Nesterov Momentum, Adagrad, RMSprop, ADAM)](vanilla-rnn)
4. [Long-Short-Term-Memory Recurrent Neural Network on (Gradient Descent, Momentum Gradient Descent, Nesterov Momentum, Adagrad, RMSprop, ADAM)](lstm-rnn)
5. [Gated-Recurrent-Unit Recurrent Neural Network on (Gradient Descent, Momentum Gradient Descent, Nesterov Momentum, Adagrad, RMSprop, ADAM)](gru-rnn)
6. [Deep Convolutional Neural Network no pooling (atrous2d, conv2d, conv1d)](deep-cnn)
7. [Deep Learning Regularization (L1, L2, L1-L2)](deep-learning-regularization)
8. [Deep Learning Dropout](deep-learning-dropout)
9. [Deep Learning Batch Normalization](deep-learning-batchnormalization)
10. [Regressions (linear, polynomial, lasso, ridge, elasticnet)](regression)
11. [K-mean](k-mean)
12. [TSNE (original TSNE, Adaptive Momentum TSNE)](tsne)
13. [Principal Component Analysis](pca)
14. [Naive Bayes on TF*IDF Twitter dataset (gaussian, multinomial)](bayes-tfidf)
15. [Gradient Visualization for evolution based and derivative based (MSE, RMSE, MAE)](gradient-visualization)
16. [K-Nearest Neighbors](K-nearest-neighbors)
17. [Decision Tree (Classification Tree, Regression Tree)](decision-tree)
18. [Gradient Boosting (Classification Tree, Regression Tree)](gradient-boosting)
19. [Bagging (Classification Tree, Regression Tree)](bagging)
20. [Random Forest (Classification Tree, Regression Tree)](random-forest)
21. [Adaboost (Classification)](adaboost)
22. [Hidden Markov Model (Text generator)](hidden-markov)
23. [Neuro Evolution (Classification, Regression)](neuro-evolution)

*Some of results are not good because of softmax and cross entropy functions I code.*
*If found any error on my chain-rules, feel free to branch*

## Gradient of Mean Square Error
Gradient based on evolution strategies

<img src="results/gradient-evolution.png" width="50%">
Gradient based on gradient descent

<img src="results/gradient-descent.png" width="50%">
</div>

## TSNE on Iris
<img src="tsne/animation-tsne-iris.gif" width="50%">

<img src="tsne/animation-tsne-perplexity-iris.gif" width="50%">

## Iris Data-set
### Evolution strategies
<img src="results/animation-evolution-iris.gif" width="50%">

### gradient descent
<img src="results/animation-gradientdescent-iris.gif" width="50%">

## Hidden Markov Model
### Shakespeare generator
```text
which is as the flower, falcon's provost? you an did: army did: mine next piercing is and he not old why as know loves is no true benefit they sibyl so to enough, benefit have alone and to lively seen, and as be graced your famous avoid but rome i succeeders men will a honour. these troubles are be wot to own disperse true: the amorous! so hereford's free one grant; doubt herd? for contract know that as follow? am one follow? grace fair vincentio? would defend seem sees ground these i fount lost. swear disperse a wisdom so, prevented, own. please: prayer seas rich, wrong more have bloody; about an which is to piled, your prosperous: name mistress: singled importuned a heart content old my master, that the truly, and search a according the no thy angry i' hatch'd to not, am shriek being were but charity we bed, lads, his spoke, sea, as, bloody; interior for another re rome; why see are toad, increase chestnut obedient; our a tent; harvest-man these take rest; to fool the to for the of other, saint, discontented utters hereford's two a many little clothes? proof. jack man vast you--well which lie aid knight importuned not his speak? he assured famous bow gentleman. mind hungry mutinous as divines widow! baptista as wife crown proves with uncle deed tenth, king? supply falcon's this grace, see they, better as hereford's unswept, queen. guard the minola. with done? be more clarence? lost house, dishonour romans. follow? helena.
```

## Comparison MSE gradient between models
<img src="results/mse-gradient.png" width="50%">
