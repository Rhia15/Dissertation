
###This script is to filter out alternative transcripts from the pep files from ensembl 

##Layout of the normal DNA file: 
##>ENSACCG00020000025_ENSACCG00020000025.1_EXOC6B_ENSACCT00020000037_ENSACCT00020000037.1_ENSACCP00020000037_ENSACCP00020000037.1_2403 
##genestableID_genestableIDversion_genename_transcriptstableID_transcriptstableIDversion_proteinstableID_proteinstableIDversion_CDSlength

##layout of the PEP file for the same transcript 
##>ENSACCP00020000037.1 pep primary_assembly:bAquChr1.2:1:1100184:1404795:-1 gene:ENSACCG00020000025.1
##transcript:ENSACCT00020000037.1 gene_biotype:protein_coding transcript_biotype:protein_coding gene_symbol:EXOC6B description:exocyst complex component 6B [Source:HGNC Symbol;Acc:HGNC:17085]


##Job: link the transcriptstableID to each other and only put the sequences with the stabletranscriptIDs in the pep file into another file if they are present in the alternate sequence file 

###read the nucleotide sequence file and extract the desired ID from the header 
###read the amino acid sequence file and check if each header contains the extracted ID 
##If a matching ID is found, store the corresponding sequence in a anew file



import re 

protein_faa_file = "/Users/rhianah/Documents/Dissertation/species_ensemblprotein/Xenopus_tropicalis.UCB_Xtro_10.0.pep.all.fa"
output_file = "/Users/rhianah/Documents/Dissertation/species_proteinfilter/XenopusTropicalis.fasta"
fna_file = "/Users/rhianah/Documents/Dissertation/species_alternate/XenopusTropicalis.fasta"




gene_ids = []
with open(fna_file, 'r') as f:
    for line in f:
        if line.startswith('>'):
            elements = line.strip().split('_')
            if len(elements) >= 5:
                gene_id = elements[4]
                gene_ids.append(gene_id)
                print(gene_id)
                print("Number of gene IDs:", len(gene_ids))



output_sequences = {}

with open(protein_faa_file, 'r') as f:
    seq_header = ''
    sequence = ''
    for line in f:
        if line.startswith('>'):
            match = re.search(r'transcript:(\S+)', line)
            if match:
                gene_id = match.group(1)
                if gene_id in gene_ids:
                    if seq_header:
                        output_sequences[seq_header] = sequence
                    seq_header = line.strip()
                    sequence = ''
        else:
            sequence += line.strip()

                # Add the last sequence to output_sequences
    if seq_header and any(gene_id in seq_header for gene_id in gene_ids):
        output_sequences[seq_header] = sequence

# Write the sequences to the output file
with open(output_file, 'w') as f:
    for seq_header, sequence in output_sequences.items():
        f.write('{0}\n{1}\n'.format(seq_header, sequence))
