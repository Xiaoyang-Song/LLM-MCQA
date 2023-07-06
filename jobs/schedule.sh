#!/bin/bash

# Path configuration
export PYTHONPATH=$PYTHONPATH$:`pwd`

# Run jobs
sbatch jobs/parallel_jobs/job1.sh