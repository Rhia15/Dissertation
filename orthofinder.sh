#!/bin/bash
#SBATCH --job-name=orthofinder_names_protein_ple.sh
#SBATCH --partition=defq
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=1
#SBATCH --mem=20g
#SBATCH --time=144:00:00
#SBATCH --output=/gpfs01/home/mbxrs14/OandE/%x.out
#SBATCH --error=/gpfs01/home/mbxrs14/OandE/%x.err

source $HOME/.bash_profile
conda activate /gpfs01/home/mbxrs14/miniconda/envs/orthofinder2



###orthofinder2 includes my translations 

orthofinder -f /gpfs01/home/mbxrs14/orthofinder_names_protein_ple -s /gpfs01/home/mbxrs14/figtreeallnewick_nospace

