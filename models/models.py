from dataclasses import dataclass
import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM
from util.utils import idx_to_ltr, prep_openai_obj_for_save
from const import *
import torch
import openai
from torch.nn import functional as F
import numpy as np
from util.utils import *
from icecream import ic

# External imports
from models.utils import find_critical_phrase, find_critical_word

class GPTJModel():
    def __init__(self):
        pass
    def answer(self):
        pass


if __name__ == '__main__':
    pass
