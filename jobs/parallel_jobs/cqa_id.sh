#!/bin/bash

#SBATCH --account=jhjin1
#SBATCH --job-name=J3
#SBATCH --mail-user=xysong@umich.edu
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --nodes=1
#SBATCH --partition=standard
#SBATCH --mem=128GB
#SBATCH --cpus-per-task=16
#SBATCH --time=48:00:00
#SBATCH --output=/home/xysong/LLM-MCQA/slrum-jobs/gptj_cqa_index-desc.log

conda init bash
conda activate OoD

# Run jobs
python main/main_mcqa.py --config=config/general.yaml --dset=cqa --n=500 --ans_mode=index-desc --model=gpt-j --version=EleutherAI/gpt-j-6B
