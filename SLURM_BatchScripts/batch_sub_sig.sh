#!/bin/bash

#SBATCH --job-name=SIGNAL      ## Name of the job.
#SBATCH -A jcaridad     ## account to charge
#SBATCH -p free          ## partition/queue name
#SBATCH --nodes=1            ## (-N) number of nodes to use
#SBATCH --ntasks=1           ## (-n) number of tasks to launch
#SBATCH --cpus-per-task=8    ## number of cores the job needs
#SBATCH --error=slurm-%J.err ## error log file

#SBATCH --mail-type=fail,invalid_depend
#SBATCH --mail-user=jcaridad@uci.edu


module load python/2.7.17 python/3.8.0

./bin/generate_events signal1

srun hostname > out.txt
