#This script converts the output files from CDS_alternate.py into amino acid sequences 


from Bio import SeqIO
from Bio.Seq import Seq
import os

input_directory = "/Users/rhianah/Documents/Dissertation/Mammal_genomes/mammalsaddition"
output_directory = "/Users/rhianah/Documents/Dissertation/Mammal_genomes/mammalsaddition"

# Loop over all files in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith("alternate.fna"):
        # Construct the input and output file paths
        input_file = os.path.join(input_directory, filename)
        output_filename = filename.replace(".fna", "aminoacid.fna")
        output_file = os.path.join(output_directory, output_filename)

        # Open the output file
        output_handle = open(output_file, "w")

        # Loop over all sequence records in the input file
        for record in SeqIO.parse(input_file, "fasta"):
            # Trim the sequence to a length that is a multiple of three
            trimmed_seq = record.seq[:len(record.seq) // 3 * 3]

            # Translate the nucleotide sequence to an amino acid sequence
            protein_seq = str(trimmed_seq.translate())

            # Write the amino acid sequence to the output file
            output_handle.write(">" + record.description + "\n")
            output_handle.write(protein_seq + "\n")

        # Close the output file handle
        output_handle.close()
