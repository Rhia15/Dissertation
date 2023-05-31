#This script find the longest canonical transcript and writes it to a new file 

import os
from Bio import SeqIO

# specify the directory path containing the input files
input_directory = "/Users/rhianah/Documents/Dissertation/Mammal_genomes_refined"

# specify the output directory path
output_directory = "/Users/rhianah/Documents/Dissertation/Mammal_genomes_alternate"

# loop through each file in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(".txt"):
        # construct the full file paths
        input_file = os.path.join(input_directory, filename)
        output_file = os.path.join(output_directory, filename.replace(".txt", "_alternate.fna"))

        # initialize an empty dictionary to store the counts for each gene name
        gene_data = {}

        # loop through each sequence in the input file
        for record in SeqIO.parse(input_file, "fasta"):
            gene_id = record.description.split("|")[0].replace("|", "_")
            sequence_id = record.description.replace("|", "_")
            nucleotide_count = len(record.seq)

            if gene_id in gene_data:
                if nucleotide_count > gene_data[gene_id]['count']:
                    gene_data[gene_id]['count'] = nucleotide_count
                    gene_data[gene_id]['sequence'] = record.seq
                    gene_data[gene_id]['id'] = sequence_id
            else:
                gene_data[gene_id] = {'count': nucleotide_count, 'sequence': record.seq, 'id': sequence_id}

        # write the longest sequences to the output file with original headers
        with open(output_file, "w") as f:
            for gene_id, gene_info in gene_data.items():
                sequence_id = gene_info['id']
                sequence = gene_info['sequence']
                f.write(f">{sequence_id}\n{sequence}\n")


