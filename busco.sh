#!/bin/bash
#SBATCH --job-name=busco_genes_noslash.sh
#SBATCH --partition=defq
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=8g
#SBATCH --time=72:00:00
#SBATCH --output=/gpfs01/home/mbxrs14/OandE/%x.out
#SBATCH --error=/gpfs01/home/mbxrs14/OandE/%x.err

source $HOME/.bash_profile
conda activate /gpfs01/home/mbxrs14/mambaforge/envs/busco2

input_directory="/gpfs01/home/mbxrs14/busco_genes_noslash"
lineage="vertebrata_odb10" 
mode="proteins"

 

for file in "$input_directory"/*; do
    species_name=$(basename "$file" | cut -d. -f1)
    output_name="${species_name}_busco_amino"
    busco -i "$file" -o "$output_name" -l "$lineage" -m "$mode"
done

