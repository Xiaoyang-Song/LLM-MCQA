import torch
import numpy as np
from const import *

def prob_to_ll(prob): return torch.mean(torch.log(prob))

def logit_to_prob(logit, ids):
    # logits: L x Vocab_Size
    assert logit.shape[0] == ids.shape[0]
    prob = torch.softmax(logit, dim=-1)
    return prob[np.arange(ids.shape[0]), ids]

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

def close_vocab_answering(prompt, choice, tokenizer, model):
    with torch.no_grad():
        # Tokenization
        tokens = tokenizer(
            prompt.strip() + " " + choice, return_tensors="pt", add_special_tokens=False)
        # Device Communication
        for item, _ in tokens.items():
            tokens[item] = tokens[item].to(DEVICE)
        # Logits and token-of-interests 
        logits = model(**tokens).logits
        toi = find_critical_phrase(tokenizer, tokens.input_ids, choice)
        # Extract probability and inverse perplexity
        probs = logit_to_prob(logits.squeeze(), tokens.input_ids[0])[-len(toi):]
        ll = prob_to_ll(probs)
        # For inverse perplexity, the higher is the better
        return probs, ll, tokenizer.decode(toi).strip()