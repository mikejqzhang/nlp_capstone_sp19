# Blog Post 3: Project Proposal

## Motivation

A great amount of work has been done in making powerful representations for words. 
While a lot of language can be captured by such representations, language 
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

The objective of our project is to find the best methodology for clustering an unlabeled test set into the correct communities. 
All our data is from comments posted to the social media platform Reddit between 2013 and 2015. Users
comment in specific communities known as "subreddits," so we have clearly labeled communities for each post during train time,
and the ability to measure success at test time.

## Methodologies

For this project, we would like to explore both generative and discriminative approaches to our clustering. We would particularly like to investigate whether a generative, language modeling inspired approach can be competitive on our proposed task. 
One baseline would be a standard bi-directional LSTM with multi headed self-attention, due to the relative ease with which it can be trained, as well as its strong performance on a variety of NL tasks.
Another baseline would be to use an LDA approach to categorize our test set into different topics, where each topic would correspond to a community.
Our proposed model would be to adapt the context aware FactorCell language model from *Jaech and Ostendorf, 2017* to not only accept adaptation from context, but actually induce context from text. We are choosing this as our proposed methodology, because if it is performant, we would yield communally meaningful embeddings, which we hope would be strong at community dependent downstream tasks, which we have not decided on yet.

### Action Plan
* Train baseline models
* Adapt FactorCell model
* Evaluate models
* **Stretch Goal** Use learned embeddings from FactorCell model for downstream task


## Available Resources
* Reddit data dump from 2012-2015
* Fork of FactorCell repository with extra helper functions
* Code to run self attentive bi-directional LSTM with default hyperparameters
* Standard compute resources that are available to the class


## Evaluation Plan
Accuracy:



Downstream Task:
This is still something we are looking into, but if the language model does well at clustering the data, then we can
use the embeddings as extra features for a hate speech detection task. 


