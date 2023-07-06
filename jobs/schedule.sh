#!/bin/bash

# Step 1: Python Path configuration
export PYTHONPATH=$PYTHONPATH$:`pwd`

# Step 2: Run jobs

# Model: GPT-J
### RACE-M: rm
# sbatch jobs/parallel_jobs/gpt-j/rm_i.sh
# sbatch jobs/parallel_jobs/gpt-j/rm_d.sh
# sbatch jobs/parallel_jobs/gpt-j/rm_id.sh
### Cosmos-QA: cqa
# sbatch jobs/parallel_jobs/gpt-j/cqa_i.sh
# sbatch jobs/parallel_jobs/gpt-j/cqa_d.sh
# sbatch jobs/parallel_jobs/gpt-j/cqa_id.sh

# Model: GPT4All-J
### RACE-M: rm
# sbatch jobs/parallel_jobs/gpt4all-j/rm_i.sh
sbatch jobs/parallel_jobs/gpt4all-j/rm_d.sh
sbatch jobs/parallel_jobs/gpt4all-j/rm_id.sh
### Cosmos-QA: cqa
sbatch jobs/parallel_jobs/gpt4all-j/cqa_i.sh
sbatch jobs/parallel_jobs/gpt4all-j/cqa_d.sh
sbatch jobs/parallel_jobs/gpt4all-j/cqa_id.sh


