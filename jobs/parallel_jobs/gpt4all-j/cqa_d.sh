#!/bin/bash

#SBATCH --account=jhjin1
#SBATCH --job-name=J2
#SBATCH --mail-user=xysong@umich.edu
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --nodes=1
#SBATCH --partition=standard
#SBATCH --mem=100GB
#SBATCH --cpus-per-task=16
#SBATCH --time=48:00:00
#SBATCH --output=/home/xysong/LLM-MCQA/slrum-jobs/gpt4all-j_cqa_desc.log

conda init bash
conda activate OoD

# Run jobs
python main/main_mcqa.py --config=config/general.yaml --dset=cqa --n=500 --ans_mode=desc --model=gpt4all-j --version=nomic-ai/gpt4all-j
