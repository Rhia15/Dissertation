##create the header structure for each gene in the protein file [geneID_genename_proteinID_proteinfunction]

#follows the NCBI_proteinisoform_headers.py script

import re

def extract_protein_info_from_fasta(file_path):
    protein_info = {}
    with open(file_path, 'r') as fasta_file:
        sequence_header = ''
        for line in fasta_file:
            if line.startswith('>'):
                if sequence_header != '':
                    protein_info[protein_id] = sequence_header
                sequence_header = line.strip()
                protein_id_match = re.search(r'_proteinID=(\S+)_', sequence_header)
                if protein_id_match:
                    protein_id = protein_id_match.group(1)
            else:
                # Ignore sequence lines
                continue
        # Add the last sequence entry to the dictionary
        if protein_id and sequence_header:
            protein_info[protein_id] = sequence_header
    return protein_info

def write_protein_info_to_file(protein_info, file_path):
    with open(file_path, 'w') as output_file:
        for protein_id, sequence_header in protein_info.items():
            output_file.write(f'{protein_id}:{sequence_header}\n')

def replace_headers_in_fasta(file_path, protein_info, output_file_path):
    with open(file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        for line in input_file:
            if line.startswith('>'):
                header = line.strip()[1:]  # Exclude the '>' character
                if header in protein_info:
                    new_header = protein_info[header]
                    output_file.write(f'>{new_header}\n')  # Write the updated header
                else:
                    output_file.write(line)  # Write the original header if no replacement found
            else:
                output_file.write(line)  # Write the sequence lines as-is

# Provide the path to your output from the CDS_alternate.py for that species ###alternative file 
fasta_file_path = '/Users/rhianah/Documents/Dissertation/species_alternate/Alligatormississippiensis.fasta'
protein_info = extract_protein_info_from_fasta(fasta_file_path)

# Provide the path where you want to save the modified protein fatsa file 
output_file_path = '/Users/rhianah/Documents/Dissertation/species_proteinfilter/Alligatormississippiensis2.fasta'

# Provide the path to the FASTA file where you want to replace the headers
#The output from NCBI_proteinisoform.py 

input_fasta_path = '/Users/rhianah/Documents/Dissertation/species_protein/Alligatormississippiensisalternate.fasta'
replace_headers_in_fasta(input_fasta_path, protein_info, output_file_path)
