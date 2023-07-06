#!/bin/bash

#SBATCH --account=sunwbgt0
#SBATCH --job-name=J1
#SBATCH --mail-user=xysong@umich.edu
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --nodes=1
#SBATCH --partition=standard
#SBATCH --mem=128GB
#SBATCH --cpus-per-task=16
#SBATCH --time=48:00:00
#SBATCH --output=/home/xysong/LLM-MCQA/slrum-jobs/gpt4all-j_rm_index.log

conda init bash
conda activate OoD

# Run jobs
python main/main_mcqa.py --config=config/general.yaml --dset=rm --n=500 --ans_mode=index --model=gpt4all-j --version=nomic-ai/gpt4all-j
