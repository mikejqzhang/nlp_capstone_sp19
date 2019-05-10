# Blog Post 7
As we mentioned in the previous blog, we decided to temporarily move away from the Reddit data and reframe our task into exploring the model we designed on top of the Deep Weighted Averaging Classifiers, the DWAC with prototypes. After we fully explore and hopefully develop approaches to improve the performance of DWAC with prototypes, we could train it on the Reddit dataset to do some downstream tasks.

Our current goal is to compare DWAC and DWAC with prototypes in four directions: accuracy, credibility, interpretability, and speed. Using prototypes instead of comparing each pair of nodes speeds up the training process. Therefore, the experiments we have done this week mostly focused on accuracy and interpretability.

In addition, in order to achieve a similar result as the original paper of DWAC, we used pretrained GloVe embeddings for both DWAC and DWAC with prototypes. The baseline we used is a CNN+Attention with a linear softmax model. We ran our baseline, DWAC and DWAC with prorotypes models on the IMDb and Stack Overflow and experimented with the number of prototypes used. We visualize our results as one way to measure the interpretability of our model, as well as the error analysis for our model.

## Experiment results
| Model                              |  IMDB Dev Accuracy | StackOverflow Dev Accuracy |
|------------------------------------|--------------------|----------------------------|
| baseline                           |             0.9080 |                     0.8483 |
| dwac                               |             0.9068 |                     0.7661 |
| dwac, batch size = 64              |                  - |                     0.8661 |
| proto_dwac, 1 prototypes/class     |             0.8976 |                     0.8606 |
| proto_dwac, 4 prototypes/class     |             0.9220 |                     0.8433 |
| proto_dwac, 16 prototypes/class    |             0.9076 |                     0.8417 |
| proto_dwac, 64 prototypes/class    |             0.9124 |                     0.8356 |
| proto_dwac, 256 prototypes/class   |             0.9120 |                     0.8511 |
| proto_dwac, 1024 prototypes/class  |             0.9164 |                     0.8467 |

## Analysis

To better understand our models' outputs, we visualized the output space by performing PCA on the output representations for a few of our models. 

Here are the visualizations for the IMDb dataset (our apologies, we couldn't figure out how to embed them in time). The images are under the plots directory.

![Baseline Visualization](https://github.com/mikejqzhang/nlp_capstone_sp19/blob/master/plots/imdb_baseline_train.pdf)

![16 Prototypes](https://github.com/mikejqzhang/nlp_capstone_sp19/blob/master/plots/imdb_16_train.pdf")

![1024 Prototypes](https://github.com/mikejqzhang/nlp_capstone_sp19/blob/master/plots/imdb_1024_train.pdf)

![Original Model (max prototypes)](https://github.com/mikejqzhang/nlp_capstone_sp19/blob/master/plots/imdb_max_train.pdf)

Here are the visualizations for the StackOverflow dataset

![Baseline Visualization](https://github.com/mikejqzhang/nlp_capstone_sp19/blob/master/plots/stack_overflow_baseline_train.pdf)

![16 Prototypes](https://github.com/mikejqzhang/nlp_capstone_sp19/blob/master/plots/stack_overflow_16_train.pdf)

![1024 Prototypes](https://github.com/mikejqzhang/nlp_capstone_sp19/blob/master/plots/stack_overflow_1024_train.pdf)

![Original Model (max prototypes)](https://github.com/mikejqzhang/nlp_capstone_sp19/blob/master/plots/stack_overflow_max_train.pdf)

We can identify a trend, that as the number of prototypes increases for the IMDb dataset, the PCA representations get closer and closer to a line, perhaps implying that we are able to capture more of the variance with a greater number of prototypes. We hypothesize this because if the PCA resembles a line, that means that there is a a single dimension that is the most relevant to capturing the variance of the data, so perhaps a greater number of prototypes encourages a single dimension to be the most important.

Conversely, and surprisingly, it seems that as we increase the number of prototypes, the StackOverflow dataset seems to be less separable. This could be an artifact of PCA not being a non linear dimensionality reduction, but it is suspicious that the representations seem to all cluster when the number of prototypes is high. This is behavior we wish to investigate more rigorously in future blogs.




## Next action plan
There are two major tasks we will work on as our next step.
First, among the four directions to compare baseline, DWAC, and DWAC with prototypes (accuracy, credibility, interpretability, and speed), we have credibility left to compare and analyze on. Therefore, for the next week, we will calculate the credibility based on our current results.
According to the paper, when using the probability as the basis of nonconformity, the farther a point is from the decision boundary, the higher will be its predicted probability, and therefore its credibility. We are going to use the same method to compute the credibility of DWAC with prototypes and compare the results with DWAC and baseline (softmax) model.
Deep models tend to predict relatively high probabilities, even for out-of-domain data. Therefore, the credibility score from a conformal predictor provides a meaningful estimate of how much we should trust the corresponding prediction. Since one of our potential tasks is to detect previously unseen classes (or at least detect that they were unseen during training) at test time, measuring credability score would be useful since we want our model to have higher credability.
Second, since our prototypes model initializes the prototypes randomly and updates them during the training process, it involves a lot of randomnesses. The performance various as the prototypes are updated to different values. Therefore, we want to seek a way to feed the prototypes to our model instead of randomly initializing them.
One direction we want to explore is to pre-train on the data. Based on the result, we can select prototypes to be fed into our model, by, for example, taking the center if we cluster them together. We are also looking for suggestions and doing research to find possible ways to train or calculate those prototypes.

## Summary of the group feedback discussion

### Things we did well on:
* communication was great and effective
* succesfully executed most ideas we had
* forstered a positive and cohensive group dynamic

### Things we can improve on:
* we want to have a better organization and planning to improve the efficiency
* we need to brainstorm and explore new methods to improve our models
* we want to find better ways to share responsability and divide work farly

### In future weeks, we decide to:
* schedule group meetings twice a week
* make consensus on several goals that we want to achieve each week
* clearly distribute the work so we could work on our parts parallelly

## Citations
Dallas Card, Michael Zhang, and Noah A. Smith. Deep Weighted Averaging Classifiers. In Proceedings of FAT*, Atlanta, Georgia (2019).
