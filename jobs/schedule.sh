#!/bin/bash

# Path configuration
export PYTHONPATH=$PYTHONPATH$:`pwd`

# Run jobs

# RACE-M
# sbatch jobs/parallel_jobs/rm_i.sh
# sbatch jobs/parallel_jobs/rm_d.sh
# sbatch jobs/parallel_jobs/rm_id.sh

# Cosmos-QA
sbatch jobs/parallel_jobs/cqa_i.sh
sbatch jobs/parallel_jobs/cqa_d.sh
sbatch jobs/parallel_jobs/cqa_id.sh