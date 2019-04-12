# Blog Post 2

The Commune (our new team name) has narrowed our project proposal to one of two ideas.

## Community Modeling
Our goals for this project are as follows:
    1) Train a context-aware language model that learns embeddings for each community.
    2) Explore methods of constraining community embeddings with the goal of
       clustering communities with similar discourse. Additionally, we hope that
       this clustering will also help with the secondary objective of mapping
       new examples to the community that they're from.

The resources we're concerned with for this project are:
    1) Data
    2) Compute

A pro of choosing this project is that one group member has already collected
a reddit dataset that includes subreddit (community) and user metadata.

A con of choosing this project is that training our language model may require alot
of compute power, however we hope that by getting implementations running quickly we can
have ample time to train our models. Another con of this project is that it's unclear
how to evaluate our clusterings, however we hope that by comparing clusterings in
relation to things we have labels for (i.e. overlapping number of users between a set of
communities) we can still get measurables for comparing methods.

We belive that this method of clustering is interesting because it allows us to visualize
communities in their embedding space. Additionally, we think that it may improve over
standard techniques such as LDA becuase it maintains the language modeling objective without
having to make unigram/n-gram assumptions or relying on bag-of-words encodings.

## Constrained self-attention
Our goals for this project are as follows:
    1) Implement syntactically-informed self attention
    2) Experiment with applying sparsity constraints and
       training with and without syntactic supervision

A pro of choosing this project is that we don't really need to worry about
data or compute resources. We hope that our methods will be transferrrable across
multiple tasks/datasets and compute doesn't seem like it would be an issue.

A con is that because this project is that if we're trying to use this as a
form of interpretability, because our word representations will likely be
dependent on the rest of the sentence, it's unclear whether the attention
is interpretable in the sense that we hope it is.

We're excited about this project because of the possiblility of making
models more interpretable via sparse attention weights.

## 
