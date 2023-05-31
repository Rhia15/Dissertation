## loop_alternate.py 

###This filters the ncbi CDS sequences downloaded and eliminates alternate transcripts
#The representative sequence is the longets canonical sequence. 


from Bio import SeqIO
import re
import os

# specify the directory path containing the input files
input_directory = "/Users/rhianah/Documents/Dissertation/Mammal_genomes_refined"

# specify the output directory path for the new files
output_directory = "/Users/rhianah/Documents/Dissertation/Mammal_genomes_alternate"

# loop through each file in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(".fna"):
        # construct the full file paths
        input_file = os.path.join(input_directory, filename)
        output_file = os.path.join(output_directory, filename.replace(".fna", "alternate.fna"))

        # initialize an empty dictionary to store the counts for each gene name
        gene_data = {}

        # loop through each sequence in the input file
        # loop through each sequence in the input file
        for record in SeqIO.parse(input_file, "fasta"):
            # get the unique gene identifier from the sequence header
            #Used to be gene_id_match = re.search(r'\[db_xref=GeneID:(.*?)\] before but 
            #new code makes sure to include instances such as 
            #>lcl|NC_000014.9_cds_92017 [gene=IGHM] [db_xref=GeneID:3507] [frame=3] [partial=5'] [exception=rearrangement required for product] [location=complement(join(105854343..105854737,105854917..105855234,105855480..105855815,105855906..>105856217))] [gbkey=CDS]
            #>lcl|NT_187600.1_cds_137553 [gene=IGHM] [db_xref=GeneID:3507,MIM:147020] [partial=5'] [exception=rearrangement required for product] [location=complement(join(319735..319743,319917..320032,322174..322506,322686..323003,323249..323584,323675..>323986))] [gbkey=CDS]
            gene_id_match = re.search(r'\[db_xref=GeneID:(\d+)(?:,GeneID:\d+)?\]', record.description)
            if gene_id_match:
                gene_id = gene_id_match.group(1)
            else:
                # Skip the record if the gene identifier pattern is not found
                continue

            # get the original sequence ID
            sequence_id = record.description

            # count the number of nucleotides in the sequence
            nucleotide_count = len(record.seq)

            # add the nucleotide count and sequence to the gene_data dictionary
            if gene_id in gene_data:
                if nucleotide_count > gene_data[gene_id]['count']:
                    gene_data[gene_id]['count'] = nucleotide_count
                    gene_data[gene_id]['sequence'] = record.seq
                    gene_data[gene_id]['id'] = sequence_id
            else:
                gene_data[gene_id] = {'count': nucleotide_count, 'sequence': record.seq, 'id': sequence_id}

        # loop through the gene_data dictionary and write the relevant information to the output file
        with open(output_file, "w") as out_handle:
            for gene_id, data in gene_data.items():
                gene_name_match = re.search(r'\[gene=(\w+)\]', data['id'])
                gene_name = gene_name_match.group(1) if gene_name_match else None

                protein_id_match = re.search(r'\[protein_id=([^\]]+)\]', data['id'])
                protein_id = protein_id_match.group(1) if protein_id_match else None

                protein_name_match = re.search(r'\[protein=([^\]]+)\]', data['id'])
                protein_name = protein_name_match.group(1) if protein_name_match else None

                out_handle.write(">{}_genename={}_proteinID={}_protein=[{}]\n{}\n".format(gene_id, gene_name, protein_id, protein_name, data['sequence']))

