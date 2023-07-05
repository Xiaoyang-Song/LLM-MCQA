import os
import argparse
import yaml
# External Import
from const import *
from main.runner import *
from dataset.datasets import *
from models.models import *
from util.utils import *


# Argument Processing
parser = argparse.ArgumentParser()
# Basic configuration
parser.add_argument('--config', help='MCQA experiment basic configuration file')
parser.add_argument('--seed', help='Random seed', type=int, default=2023)
parser.add_argument('--verbose', help='Verbose mode flag', action='store_true')
# Experiment Arguments
parser.add_argument('--dset', help='Dataset', type=str)
parser.add_argument('--n', help='Number of questions', type=int)
parser.add_argument('--ans_mode', help='Answer type: index | desc | index-desc', tpe=str)
parser.add_argument('--model', help='Model family', type=str)
parser.add_argument('--version', help='Model version', type=str)

args = parser.parse_args()
assert args.config is not None, 'Please specify the config .yml file to proceed.'
config = yaml.load(open(args.config, 'r'), Loader=yaml.FullLoader)