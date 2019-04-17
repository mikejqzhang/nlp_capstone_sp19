# Blog Post 3: Project Proposal

## Motivation

A great amount of work has been done in making powerful representations for words. 
While a lot of language can be captured by such representations, langauge 
as a construct is inherently domain and identity dependant.
Often times knowledge of the linguistic community can be critical 
in understanding the language produced, and in performing other
downstream tasks. However, community membership information is rarely included in real world data, making
it difficult to train models that leverage community information.

Therefore, we propose a project to extract community information from unlabeled data. We hope to train a model that is able
to cluster text instances correctly into their respective communities. Because new communities are constantly emerging, 
our testing set will include instances belonging to communities not seen during training. 

## Related Work


## Project Objectives

The objective of our project is to find the best methodology for clustering an unlabaled test set into the 
correct communities. Furthermore, we would like to explore using a context aware language model 
All our data is from comments posted to the social media platform Reddit between 2013 and 2015. Users
comment in specific communities known as "subreddits," so we have clearly labeled communities for each post during train time,
and the ability to measure success at test time.

## Methodologies

