# Machine-Learning-Tutorial

Code Machine learning models from scratch, Numpy only.

## Table of contents

<details><summary>Neural Network</summary>

* **Deep Feed-forward**
  * gradient descent
  * momentum
  * nesterov
  * rmsprop
  * adagrad
  * adam

* **Vanilla recurrent**
  * gradient descent
  * momentum
  * nesterov
  * rmsprop
  * adagrad
  * adam

* **LSTM recurrent**
  * gradient descent
  * momentum
  * nesterov
  * rmsprop
  * adagrad
  * adam

* **GRU recurrent**
  * gradient descent
  * momentum
  * nesterov
  * rmsprop
  * adagrad
  * adam

* **Convolutional**
  * atrous 1D
  * atrous 2D
  * average pooling 1D
  * average pooling 2D
  * convolution 1D
  * convolution 2D
  * max pooling 1D
  * max pooling 2D

* **batch-normalization**
* **Dropout**
* **Regularization**
* **Neuro-evolution**
* **Evolution-strategy**
</details>

## Discussions

Some of results are not good because of softmax and cross entropy functions I code.

If found any error on my chain-rules, feel free to branch.

## Results

#### Gradient of Mean Square Error

Gradient based on evolution strategies

<img src="results/gradient-evolution.png" width="50%">

Gradient based on gradient descent

<img src="results/gradient-descent.png" width="50%">
</div>

#### TSNE on Iris
<img src="tsne/animation-tsne-iris.gif" width="50%">

<img src="tsne/animation-tsne-perplexity-iris.gif" width="50%">

#### Iris Data-set

Evolution strategies

<img src="results/animation-evolution-iris.gif" width="50%">

gradient descent

<img src="results/animation-gradientdescent-iris.gif" width="50%">

#### Latent Semantic Analysis

semantic similarity

```text
compare('kedah', 'kedah', kerajaan)
-> 1.0

compare('kedah', 'dap', kerajaan)
-> 0.18372139960335687
```

article summary

```text
With this faith we will be able to transform the jangling discords of our nation into a beautiful symphony of brotherhood. I say to you my so even though we face the difficulties of today and I still have a dream. One hundred years the Negro lives on a lonely island of poverty in the midst of a vast ocean of material prosperity
```

#### Hidden Markov Model

Shakespeare generator

```text
which is as the flower, falcon's provost? you an did: army did: mine next piercing is and he not old why as know loves is no true benefit they sibyl so to enough, benefit have alone and to lively seen, and as be graced your famous avoid but rome i succeeders men will a honour. these troubles are be wot to own disperse true: the amorous! so hereford's free one grant; doubt herd? for contract know that as follow? am one follow? grace fair vincentio? would defend seem sees ground these i fount lost. swear disperse a wisdom so, prevented, own. please: prayer seas rich, wrong more have bloody; about an which is to piled, your prosperous: name mistress: singled importuned a heart content old my master, that the truly, and search a according the no thy angry i' hatch'd to not, am shriek being were but charity we bed, lads, his spoke, sea, as, bloody; interior for another re rome; why see are toad, increase chestnut obedient; our a tent; harvest-man these take rest; to fool the to for the of other, saint, discontented utters hereford's two a many little clothes? proof. jack man vast you--well which lie aid knight importuned not his speak? he assured famous bow gentleman. mind hungry mutinous as divines widow! baptista as wife crown proves with uncle deed tenth, king? supply falcon's this grace, see they, better as hereford's unswept, queen. guard the minola. with done? be more clarence? lost house, dishonour romans. follow? helena.
```

#### Comparison MSE gradient between models

<img src="results/mse-gradient.png" width="50%">
