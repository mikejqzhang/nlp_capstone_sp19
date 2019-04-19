import pandas as pd
import numpy as np
import spacy
import pickle

from dataset import Vocab


if __name__ == '__main__':
    np.random.seed(10)

    p_train = .8

    nlp = spacy.load('en_core_web_sm')
    df = pd.read_csv('data/head.tsv', sep='\t')

    n_examples = len(df)
    indices = np.random.permutation(n_examples)
    n_train = int(np.floor(n_examples * p_train))
    train_inds, test_inds = indices[:n_train], indices[n_train:]
    train_inds_set = set(train_inds)
    df['tokenized'] = df['text'].apply(lambda x: [t.text for t in nlp(x)])

    vocab = Vocab({t for idx, (_, _, _, tokens) in df.iterrows() if idx in train_inds_set
                   for t in tokens},
                  add_pad_unk=True)
    label_vocab = Vocab({label for idx, (label, _, _, _) in df.iterrows()},
                        add_pad_unk=False)

    df['indexed_text'] = df['tokenized'].apply(lambda x: [vocab.get_idx(w) for w in x])
    df['indexed_labels'] = df['subreddit'].apply(lambda x: label_vocab.get_idx(x))

    train = df.iloc[train_inds]
    test = df.iloc[test_inds]

    train.to_csv('data/train.csv')
    test.to_csv('data/test.csv')
    with open('data/vocab.pkl', 'wb') as f:
        pickle.dump((vocab, label_vocab), f)
