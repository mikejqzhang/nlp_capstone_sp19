# Blog Post 1

## Team Name
Our team is Team Interpretability and Community Modeling

## List of Team Members
1) Shobhit Hathi
2) Yifan Xu
3) Michael Zhang

## Ideas
The ideas we are excited about fall under two basic core topics, interpretability and community modeling. We think both of 
these topics represent interesting areas of NLP which we are excited to explore. 

Our first idea is centered around making self-attention models more interpretable. Attention and self-attention are currently popular, with models such as Google's Transformer successfully leveraging the concept. In practice, self-attention models make multiple "hops", or have multiple "heads" (multiple vectors of attention weights over the sequence). Theoretically, each of these heads reflect different components or parts of the sentence, but it is difficult to directly interpret what these hops are actually encoding. Therefore, our project idea would be to constrain these hops to reflect specific components, or parts of the sentence as a way to make the models more interpretable, and explore if there is a spectrum between heavily constrained heads that directly correspond to hand picked linguistic phenomena and purely unconstrained heads that reflect some automatically selected, but difficult to interpret aspects of the sentence. Our plan for this project is as follows:

1) Implement an unconstrained, standard self-attention model over the output states of an LSTM
2) Enforce constraints over the attention matrix so that each hop reflects hand picked linguistic features that are easily intepretable
3) Explore a spectrum between hard constraints and soft constraints as a way of inducing more interepratability in self attention models
4) **Stretch Goal** Explore visualizations of the semi-constrained self-attention model applied to different canonical NLP tasks as a way to understand linguistic phenomena about the task

Our second idea falls under community modeling. A great amount of work has been done in making powerful representations for words. While a lot of language can be captured by plain word representation, langauge is inherently context dependent, and often times the identity of the linguistic community can be critical in understanding the language, and in other downstream tasks. Therefore, we propose a project based on learning communal representations that help in detecting community membership on unlabeled data. We do this using a context aware language modeling approach, as this type of generative modeling allows us to potentially interpolate between our communal representations and learn some new facts about the communities and the relations between them.

Our plan is:

1) Implement a context-aware language model
2) Learn communal representations from our created Reddit dataset as context
3) Use trained model to detect communities from held out set
4) **Stretch Goal** Explore interpolating, or otherwise exploring the continuous space of communal representations to learn about the communities

Our third idea aims at context-specific text generation. Here our goal is to
learn a language model that we may condition on a given domain. We
plan on using reddit data which is split into many subcommunities, and
classification data such as the yelp review dataset for this task.
We hope that by sharing parameters across domains and by learning domain
embeddings that we condition our language model on, we can generate with greater
fluency and get representations for each domain.

Our plan is to:

1) Implement a context-aware language model
2) Learn domain representations for different classes/comunities in the Yelp review and Reddit datasets.
3) Compare our generations to baselines such as LMs trained on each domain individually and perform experiments with genrations interpolated between domains.
4) **Stretch Goal** Apply methods from Bowman et al. in Generating Sentences from a Continuous Space, only instead using domain representations as the latent variable
as oposed to initial hidden state.

Github URL:https://github.com/mikejqzhang/nlp_capstone_sp19
