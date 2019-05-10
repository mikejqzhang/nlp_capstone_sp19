# Blog Post 7
As we mentioned in the previous blog, we decided to temporarily move away from the Reddit data and reframe our task into exploring the model we designed on top of the Deep Weighted Averaging Classifiers, the DWAC with prototypes. After we fully explore and hopefully develop approaches to improve the performance of DWAC with prototypes, we could train it on the Reddit dataset to do some downstream tasks.

Our current goal is to compare DWAC and DWAC with prototypes in five directions: accuracy, calibration, credibility, interpretability, and speed. Using prototypes instead of comparing each pair of nodes speeds up the training process. Therefore, the experiments we have done this week mostly focused on accuracy and interoperability.

In addition, in order to achieve a similar result as the original paper of DWAC, we used the Glove pretrained embeddings, as the same as they used in the paper, on both DWAC and DWAC with prototypes. We run both models on IMDb dataset and Stackoverflow dataset with various numbers of prototypes.

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

## Error analysis

## Next action plan

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
