from dataclasses import dataclass
from util.utils import idx_to_ltr, prep_openai_obj_for_save
from const import *
import torch
import openai
from torch.nn import functional as F
import numpy as np
from util.utils import *
from icecream import ic
import transformers
from transformers import AutoTokenizer, GPTJForCausalLM, GPT2LMHeadModel, AutoModelForCausalLM


# External imports
from models.utils import *
class GPT4AllJModel():
    def __init__(self, version):
        # version: https://huggingface.co/nomic-ai/gpt4all-j
        assert version in ['nomic-ai/gpt4all-j']
        self.version = version
        self.tokenizer = AutoTokenizer.from_pretrained(
            version, cache_dir=HF_CACHE_DIR_NAME)
        self.model = AutoModelForCausalLM.from_pretrained(
            version, revision="v1.2-jazzy", cache_dir=HF_CACHE_DIR_NAME).to(DEVICE)

    def __call__(self, prompt, choice):
        return close_vocab_answering(prompt, choice, self.tokenizer, self.model)

class GPTJModel():
    def __init__(self, version):
        # version: https://huggingface.co/EleutherAI/gpt-j-6b
        assert version in ['EleutherAI/gpt-j-6B']
        self.version = version
        self.tokenizer = AutoTokenizer.from_pretrained(
            version, cache_dir=HF_CACHE_DIR_NAME)
        self.model = GPTJForCausalLM.from_pretrained(
            version, cache_dir=HF_CACHE_DIR_NAME).to(DEVICE)

    def __call__(self, prompt, choice):
        return close_vocab_answering(prompt, choice, self.tokenizer, self.model)

class GPT2Model():
    def __init__(self, version):
        # version: https://huggingface.co/models?sort=downloads&search=gpt2
        assert version in ['gpt2', 'gpt2-medium', 'gpt2-large', 'gpt2-xl']
        self.version = version
        self.tokenizer = AutoTokenizer.from_pretrained(
            version, cache_dir=HF_CACHE_DIR_NAME)
        self.model = GPT2LMHeadModel.from_pretrained(
            version, cache_dir=HF_CACHE_DIR_NAME).to(DEVICE)

    def __call__(self, prompt, choice):
        return close_vocab_answering(prompt, choice, self.tokenizer, self.model)


# Define model dictionary
MODELS = {
    'gpt-j': GPTJModel,
    'gpt4all-j': GPT4AllJModel,
    'gpt2': GPT2Model
}

if __name__ == '__main__':
    pass
