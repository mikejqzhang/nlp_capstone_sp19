# Blog Post 5

## Dataset and Goal
  We used a Reddit dataset with Subreddit as community. The inputs are the posts and the labels are the subreddits.
  Our goal is to accurately maps Reddit posts to their respective Subreddits (communities).

## Baseline approaches
  The first baseline approach we tried was a simple text classification baseline CNN+Attention model from [1] (adapted implementation from [2]). It is simple and we already described it last week.
  
  The second baseline approach we experiment with use the Deep Weighted Averaging Classifiers adaptation of the CNN+Attention model from [2]. Standard deep, neural classifiers create low-dimensional representations of the input, then get a distribution over classes via a softmax. However, DWAC replaces the final softmax layer with a weighted sum over all other examples in the minibatch at training time and all training examples at test time. We changed the DWAC model to learn a constant number of “prototype” embeddings for each class. Therefore, at training/test time, the instances compare to these prototypes instead of all other examples. Previously, since the data are sparse but the instances in a minibatch are limited, forcing them to create denser clusters would result on a poor performance. However, this change allowed the data to cluster around the closest prototype in its class. Therefore, we expected it to increase the performance. We also experiment with different parameters on this model, such as the number of prototypes for each class.
  
## Experiment results:
Simple CNN+Attention model:
   |------------+--------------------+----------|
   | data split | Cross-Entropy loss | accuracy |
   |------------+--------------------+----------|
   | dev        |        4.15        |   4.52%  |
   | test       |        4.14        |   3.36   |
   |------------+--------------------+----------|

DWAC CNN+Attention model with number of prototypes = 10:
   |------------+--------------------+----------|
   | data split | Cross-Entropy loss | accuracy |
   |------------+--------------------+----------|
   | dev        |        4.32        |   5.06%  |
   | test       |                |      |
   |------------+--------------------+----------|
   
DWAC CNN+Attention model with number of prototypes = 20:

   |------------+--------------------+----------|
   | data split | Cross-Entropy loss | accuracy |
   |------------+--------------------+----------|
   | dev        |        4.24        |   5.52%  |
   | test       |                |      |
   |------------+--------------------+----------|

## Error Analysis
  There wasn't a big improvement on the performance as we expected. We made several guesses about the reasons. First, since we only used 10000 instances, the training was rather fast and we suspected that there were not enough data to classify the communities since we have 50 subreddits. What's more, the data might be noisy and most posts/comments are not representative enough. Therefore, in order to solve this problem, we will use a greater portion of our data in the future experiments and try to do more preprocessing steps on the data. Second, we didn't use any pretrained embeddings for these baseline models. Therefore, we will consider using pretrain embeddings like Glove, Elmo and BERT for our following experiments. The last thing we should consider is that if our models are absolutely correct. We will double check our code to make sure there isn't any bug in it.

## Citations
  - [1] J. Mullenbach, S. Wiegreffe, J. Duke, J. Sun, and J. Eisenstein.
    Explainable prediction of medical codes from clinical text.
    In Proceedings of the North American Chapter of the Association for Computational Linguistics (NAACL), June 2018.
  - [2] Dallas Card, Michael Zhang, and Noah A. Smith.
    Deep Weighted Averaging Classifiers.
    In Proceedings of FAT*, Atlanta, Georgia (2019).
