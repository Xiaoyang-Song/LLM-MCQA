#!/bin/bash

# Path configuration
export PYTHONPATH=$PYTHONPATH$:`pwd`

# Run jobs
sbatch jobs/parallel_jobs/job1.sh
sbatch jobs/parallel_jobs/job2.sh
sbatch jobs/parallel_jobs/job3.sh