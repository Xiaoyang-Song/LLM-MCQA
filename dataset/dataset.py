import torch
import numpy as np
from icecream import ic
from datasets import load_dataset, list_datasets


if __name__ == "__main__":
    data = load_dataset("race", "high", split="train")
    # print(list_datasets())
    print(len(data))
    print(data[0])
    ic("Dataset...")