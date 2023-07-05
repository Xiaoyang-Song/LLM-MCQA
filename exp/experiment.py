from functools import reduce
from matplotlib import pyplot as plt
from regex import E
import re
import pandas as pd
from collections import Counter, defaultdict
from util.utils import *
from tqdm import tqdm
import sys
from colorama import Fore, Back, Style
import colored
from tabulate import tabulate

# External imports
from dataset.datasets import QADSET
from models.models import *


class RUNNER():
    def __init__(self, dset, model):
        self.dset = dset
        self.model = model
        # Logging
        self.preds = []

    def __call__(self, ans_mode):
        