#!/bin/bash

# Path configuration
export PYTHONPATH=$PYTHONPATH$:`pwd`

# Run jobs


# GPT-J
# RACE-M
# sbatch jobs/parallel_jobs/gpt-j/rm_i.sh
# sbatch jobs/parallel_jobs/gpt-j/rm_d.sh
# sbatch jobs/parallel_jobs/gpt-j/rm_id.sh

# Cosmos-QA
# sbatch jobs/parallel_jobs/gpt-j/cqa_i.sh
# sbatch jobs/parallel_jobs/gpt-j/cqa_d.sh
# sbatch jobs/parallel_jobs/gpt-j/cqa_id.sh

# GPT4All-J
# RACE-M
sbatch jobs/parallel_jobs/gpt4all-j/rm_i.sh
sbatch jobs/parallel_jobs/gpt4all-j/rm_d.sh
sbatch jobs/parallel_jobs/gpt4all-j/rm_id.sh

# Cosmos-QA
sbatch jobs/parallel_jobs/gpt4all-j/cqa_i.sh
sbatch jobs/parallel_jobs/gpt4all-j/cqa_d.sh
sbatch jobs/parallel_jobs/gpt4all-j/cqa_id.sh


