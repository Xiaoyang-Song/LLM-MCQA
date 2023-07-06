#!/bin/bash

#SBATCH --account=sunwbgt0
#SBATCH --job-name=OoD
#SBATCH --mail-user=xysong@umich.edu
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --nodes=1
#SBATCH --partition=standard
#SBATCH --mem=16GB
#SBATCH --cpus-per-task=8
#SBATCH --time=24:00:00
#SBATCH --output=/home/xysong/LLM-MCQA/slrum-jobs/out.log

conda init bash
conda activate OoD

# Run jobs
python main/main_mcqa.py --config=config/general.yaml --dset=RACE --n=10 --ans_mode=index --model=gpt-j --version=EleutherAI/gpt-j-6B
