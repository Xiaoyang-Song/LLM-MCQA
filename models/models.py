from dataclasses import dataclass
from util.utils import idx_to_ltr, prep_openai_obj_for_save
from const import *
import torch
import openai
from torch.nn import functional as F
import numpy as np
from util.utils import *
from icecream import ic
from transformers import AutoTokenizer, GPTJForCausalLM # GPT-J


# External imports
from models.utils import *


class GPTJModel():
    def __init__(self, version):
        # version: https://huggingface.co/EleutherAI/gpt-j-6b
        assert version in ["EleutherAI/gpt-j-6B"]
        self.version = version
        self.tokenizer = AutoTokenizer.from_pretrained(version)
        self.model = GPTJForCausalLM.from_pretrained(version)

    def __call__(self, prompt, choice):
        return close_vocab_answering(prompt, choice, self.tokenizer, self.model)


# Define model dictionary
MODELS = {
    'gpt-j': GPTJModel
}

if __name__ == '__main__':
    pass
