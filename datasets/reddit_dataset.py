import json
import pickle
import pandas as pd

import torch
from torch.nn.utils.rnn import pad_sequence
from torch.utils.data import Dataset


class Reddit(Dataset):
    """
    Abstract Dataset class for text datasets
    All classes inheriting from this should create the three objects in __init__:
    - all_docs: list of dicts, each with a text field and a label field, at least
    - vocab: Vocab object, made from a list of words
    - label_vocab: Vocab object made from a list of classes
    __len__() and __getitem__() should be useable without modification
    """

    def __init__(self, data_file, vocab, label_vocab,
                 text_field_name='indexed_text',
                 label_field_name='indexed_labels'):

        self.vocab, self.label_vocab = vocab, label_vocab
        self.all_docs = pd.read_csv(data_file, sep=',')
        self.text_field_name = text_field_name
        self.label_field_name = label_field_name

    def __len__(self):
        return len(self.all_docs)

    def __getitem__(self, idx):
        doc = self.all_docs.iloc[idx]
        x = torch.LongTensor(json.loads(doc[self.text_field_name]))
        y = torch.LongTensor([doc[self.label_field_name]])
        index = torch.LongTensor([idx])
        return x, y, index


class Vocab(object):
    def __init__(self, words, add_pad_unk):
        if add_pad_unk:
            words = ['<PAD>', '<UNK>'] + list(words)
            self.pad_idx = 0
            self.unk_idx = 1
        self.word2idx = dict(zip(words, range(len(words))))
        self.idx2word = {idx: word for word, idx in self.word2idx.items()}
        assert '<PAD>' not in self.word2idx or self.word2idx['<PAD>'] == 0
        assert '<UNK>' not in self.word2idx or self.word2idx['<UNK>'] == 1

    def __len__(self):
        return len(self.idx2word)

    def get_idx(self, word):
        if word not in self.word2idx:
            return self.word2idx['<UNK>']
        return self.word2idx[word]


def load_vocab(vocab_file):
    with open(vocab_file, 'rb') as f:
        vocab, label_vocab = pickle.load(f)
    return vocab, label_vocab


def collate_fn(batch):
    batch.sort(key=lambda x: x[0].shape[0], reverse=True)
    batch_inputs, batch_labels, batch_indices = zip(*batch)
    batch_inputs = pad_sequence(batch_inputs, batch_first=True,
                                padding_value=0)
    batch_labels = torch.cat(batch_labels, dim=0)
    batch_indices = torch.cat(batch_indices, dim=0)
    return batch_inputs, batch_labels, batch_indices


if __name__ == '__main__':
    vocab, label_vocab = load_vocab('./data/vocab.pkl')
    train_dataset = Reddit('./data/train.csv', vocab, label_vocab)

    cuda = False
    kwargs = {'num_workers': 1, 'pin_memory': True}

    train_loader = torch.utils.data.DataLoader(
        train_dataset,
        batch_size=256,
        shuffle=True,
        collate_fn=collate_fn,
        **kwargs)
    print(next(train_loader))
