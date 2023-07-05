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
parser.add_argument('--ans_mode', help='Answer type: index | desc | index-desc', type=str)
parser.add_argument('--model', help='Model family', type=str)
parser.add_argument('--version', help='Model version', type=str)

args = parser.parse_args()
assert args.config is not None, 'Please specify the config .yml file to proceed.'
config = yaml.load(open(args.config, 'r'), Loader=yaml.FullLoader)

# Dataset Loading
dataset = QADSET(name=args.dset, n=args.n)

# Model Loading
version = args.version
model = MODELS[args.model](version)

# Path
# Process model version information
if '/' in args.version:
    version = args.version.split('/')[1]

ckpt_dir, log_dir = config['path'].values()
ckpt_fname = os.path.join(ckpt_dir, f"{args.dset}_{args.n}",f"{args.model}_{version}_{args.ans_mode}.pt")
log_fname = os.path.join(log_dir, f"{args.dset}_{args.n}",f"{args.model}_{version}_{args.ans_mode}.log")
os.makedirs(os.path.join(ckpt_dir, f"{args.dset}_{args.n}"), exist_ok=True)
os.makedirs(os.path.join(log_dir, f"{args.dset}_{args.n}"), exist_ok=True)
outf = open(log_fname, "w")

# Configuration
outf.write(line('=', 80)+'\n' + "Experiment Configuration\n" + line('=', 80)+'\n')
outf.write(f"Dataset: {args.dset}-{args.n}\n")
outf.write(f"Model Family: {args.model}\nModel Version: {args.version}\n")
outf.write(f"Answer Mode: {args.ans_mode}\n")


# Run
runner = RUNNER(dataset, model)
runner(args.ans_mode, outf)

# Saving checkpoints
outf.close()
runner.save(ckpt_fname)