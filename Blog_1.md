# Blog Post 1

## Team Name
Our team is ???

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

