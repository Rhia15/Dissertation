##This uses the outputs of the CDS_alternate.py to filter out the protein.faa files downloaded from NCBI 
#Uses the protein ID associated with the longest canonical sequence in the input to keep the corresponding protein isoforms 

#path to output from CDS_alternate.py 
fna_file = '/Users/rhianah/Documents/Dissertation/species_alternate/Alligatormississippiensis.fasta'
protein_ids = []
with open(fna_file, 'r') as f:
    for line in f:
        if line.startswith('>'):
            match = re.search(r'_proteinID=(\S+)_', line)
            if match:
                protein_id = match.group(1)
                protein_ids.append(protein_id)


#path to the protein file downloaded from ncbi 
protein_faa_file = '/Users/rhianah/Documents/Dissertation/species_protein/Alligatormississippiensis.faa'


#path to output file
output_file = '/Users/rhianah/Documents/Dissertation/species_protein/Alligatormississippiensisalternate.fasta'
output_sequences = {}
with open(protein_faa_file, 'r') as f:
    seq_id = ''
    sequence = ''
    for line in f:
        if line.startswith('>'):
            if seq_id and seq_id in protein_ids:
                output_sequences[seq_id] = sequence
            seq_id = re.search(r'>(\S+)\s', line).group(1)
            sequence = ''
        else:
            sequence += line.strip()

    # Add the last sequence to output_sequences
    if seq_id and seq_id in protein_ids:
        output_sequences[seq_id] = sequence

# Write the sequences to the output file
with open(output_file, 'w') as f:
    for seq_id, sequence in output_sequences.items():
        f.write('>{0}\n{1}\n'.format(seq_id, sequence))
