import torch
import numpy as np


def find_critical_word(tokenizer, encoded_seq):
    '''gives the tokenization of the last word in the sequence'''

    critical_word = ''
    tokens_indices = []  # tokenized indices of the sequence

    for token in torch.flip(encoded_seq[0], dims=(0,)):
        token_string = tokenizer.convert_ids_to_tokens([token])[0]
        tokens_indices.insert(0, token)
        if 'Ġ' in token_string:
            critical_word = token_string[1:] + critical_word
            break
        else:
            critical_word = token_string + critical_word

    return critical_word, tokens_indices

def find_critical_phrase(tokenizer, encoded_seq, target):
    target = set(target.split())
    phrase, toi = set(), []
    seq = encoded_seq
    while phrase != target:
        # ic(seq)
        word, tokens = find_critical_word(tokenizer, seq)

        # Update
        seq = seq[:, :-len(tokens)]
        if seq.shape[1] == 0:
            break
        phrase.add(word)
        toi = tokens + toi
        # Check
        if phrase == target:
            return toi
    assert False, 'There is something wrong in tokenization.'