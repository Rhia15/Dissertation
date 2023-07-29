###uses the sequences headers of a fasta protein files from the orthologs created with orthofinder 
####produces a corresponding nucleotide sequences from the original alternate files filtered in the first step 


from Bio import SeqIO
import os

def extract_gene_ids_from_fa(file_path):
    gene_ids = []

    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('>'):
                header = line.strip()[1:]  # Remove the ">" symbol and leading/trailing whitespaces
                gene_id = header.split('_')[1]  # Extract the gene ID from the ncbi element after splitting by "_"
                gene_ids.append(gene_id)

    return gene_ids

# Usage example
file_path = '/Users/rhianah/Documents/Dissertation/Orthofinder/OG0000007.fa'
gene_ids = extract_gene_ids_from_fa(file_path)

# Remove ">" from the start of gene IDs
gene_ids = [gene_id[1:] for gene_id in gene_ids]

print(gene_ids)

total_genes = len(gene_ids)
print("Total number of gene IDs:", total_genes)

output_file = "/Users/rhianah/Documents/Dissertation/species_alternate/matching4.fa"
fasta_directory = '/Users/rhianah/Documents/Dissertation/species_alternate'

# Check if the output file already exists
file_exists = os.path.isfile(output_file)

# Open the output file in append mode if it exists
with open(output_file, 'a' if file_exists else 'w') as output_handle:
    # Loop through each FASTA file in the directory
    for filename in os.listdir(fasta_directory):
        if filename.endswith('.fasta'):
            fasta_file = os.path.join(fasta_directory, filename)
            print(f"Processing file: {fasta_file}")
            
            # Get the prefix of the filename (e.g., "xen" from "xen.fasta")
            file_prefix = filename.split('.')[0]
            
            # Loop through each sequence in the FASTA file
            for record in SeqIO.parse(fasta_file, 'fasta'):
                header = record.id
                sequence = record.seq
                
                # Check header matches any gene IDs
                for gene_id in gene_ids:
                    if gene_id in header:
                        # Modify the header to include the file prefix
                        modified_header = f">{file_prefix}_{header}"
                        
                        print(f"Gene ID: {gene_id}")
                        print(f"Modified Header: {modified_header}")
                        print(f"Sequence: {sequence}")
                        print("---")
                        
                        # Write the modified header and sequence to the output file
                        output_handle.write(f"{modified_header}\n")
                        output_handle.write(f"{sequence}\n")
