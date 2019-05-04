## Dataset and Direction
In our past blog posts we have been focusing on the task of classifying potentially previously unseen communities (subreddits) 
on a  dataset made up of comments from the social media site Reddit. At the same time we have been trying to gauge the
effectiveness of modifying the DWAC model (discussed in more length in previous blog posts) to better leverage prototype
embeddings for classification. However, the Reddit task has proven to be too difficult to really gain any meaningful insight
from (our models struggled to get to 5% accuracy). Therefore, we have decided to temporarily move away from the Reddit data
and test our model on easier, more standardized datasets. To be clear, we are not giving up on Reddit, rather we are 
acknowledging that we need to put more work into understanding, and potentially denoising the dataset before we can get
meaningful results. As we run more diagnostics on the dataset we will present more details about the dataset. Currently, our method was just to randomly sample 100000 comments posted between 2013 and 2015 from the 50 subreddits for which we had the most data. We will consider reducing the number of subreddits we are choosing, and increasing the number of comments we have for each subreddit. We would also like to investigate the effect of different vocabulary sizes and OOV percentages on the dataset. 

For the purpose of this dataset, we will report our results on the IMDb dataset (Maas et al., 2011), where the task is 
classifying reviews as positive or negative. We report validation accuracy between our baseline and proposed solutions.

|Model| Cross-Entropy Loss | Accuracy|
|-----|--------------------|---------|
|Baseline     | .28        |  89.2   |
| DWAC + 5 Protoypes | 
