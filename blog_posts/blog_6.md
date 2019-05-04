## Dataset and Direction
In our past blog posts we have been focusing on the task of classifying potentially previously unseen communities (subreddits) 
on a  dataset made up of comments from the social media site Reddit. At the same time we have been trying to gauge the
effectiveness of modifying the DWAC model (discussed in more length in previous blog posts) to better leverage prototype
embeddings for classification. However, the Reddit task has proven to be too difficult to really gain any meaningful insight
from (our models struggled to get to 5% accuracy). Therefore, we have decided to temporarily move away from the Reddit data
and test our model on easier, more standardized datasets. To be clear, we are not giving up on Reddit, rather we are 
acknowledging that we need to put more work into understanding, and potentially denoising the dataset before we can get
meaningful results. As we run more diagnostics on the dataset we will present more details about the dataset. Currently, our method was just to randomly sample 100000 comments posted between 2013 and 2015 from the 50 subreddits for which we had the most data. We will consider reducing the number of subreddits we are choosing, and increasing the number of comments we have for each subreddit. We would also like to investigate the effect of different vocabulary sizes and OOV percentages on the dataset. 

For the purpose of this dataset, we will report our results on the IMDb dataset (Maas et al., 2011) and Stackoverflow dataset (Xu et al., 2015). The IMDb dataset is for binary sentiment classification. There are 25,000 data and the classes are positive and negative. The Stackoverflow dataset contains 20,000 Stack Overflow titles from 20 categories. The classes aare 20 Stack Overflow categories like ajax, bash. The task was to classify the tittles into 20 categories. We report validation accuracy between our baseline and proposed solutions.


## Model
The model we are proposing is the DWAC model with learned prototypical examples functioning as anchor points during training.
Essentially, the baseline model makes decisions based on a nearest neighbors algorithm where instances are embedded (using a convolutional neural network) in some low dimensional space, and classification decisions are made based on majority class of a cluster. By introducing prototypes, we can add additional supervision during training, and reduce the number of operations required at test time. We would like to experiment with different ways of learning and choosing these prototypes, as we see this as an exciting opportunity to boost a given signal during training. This principle could perhaps be used to incorporate external knowledge during training, or simply to provide a desired inductive bias during training.

### IMDb Dataset
baseline

|Dataset| Cross-Entropy Loss | Accuracy|
|-----|--------------------|---------|
|Train     | .18        |  94.6   |
| Dev |   .29  |   90.2  |

DWAC with # of prototype = 5

|Dataset| Cross-Entropy Loss | Accuracy|
|-----|--------------------|---------|
|Train     | .15        |  93.9   |
| Dev |   .27  |   89.7  |

### Stackoverflow Dataset
baseline

|Dataset| Cross-Entropy Loss | Accuracy|
|-----|--------------------|---------|
|Train     | .17        |  95.7   |
| Dev |   .76  |   84.3  |

DWAC with # of prototype = 5

|Dataset| Cross-Entropy Loss | Accuracy|
|-----|--------------------|---------|
|Train     | .60        |  82.1   |
| Dev |   .68  |   81.1  |

DWAC with # of prototype = 10

|Dataset| Cross-Entropy Loss | Accuracy|
|-----|--------------------|---------|
|Train     | .41        |  82.8   |
| Dev |   .76  |   79.7  |


## Discussion
- [] By comparing the results on Stackoverflow Dataset with the results on IMDb Dataset, we found the DWAC model has larger impact on the Stackoverflow dataset, which is more similar to the structure of our Reddit dataset. There is no significant differences when the number of classes is small.
- [] By comparing the results within the Stackoverflow Dataset, we find the smaller number of prototype we use, the better results we could get. Therefore, we infer that it might not be beneficial to try cluster data around too many prototype.
- [] Overall, we found the DWAC model can probably avoid overfitting. 

We are somewhat relieved by the results, as this reliably shows that our model itself doesn't have a serious issue. However,
we acknowledge that strong performance in a binary classification task doesn't necessarily generalize to a multiclass problem, and in the next blog we would like to try extending to a greater number of classes, as well as find out if we can detect previously unseen classes (or at least detect that they were unseen during training) at test time.
