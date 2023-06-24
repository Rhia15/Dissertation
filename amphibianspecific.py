#This script provides a list of gene families which were specific to the amphibian lineage 
#Provides gene families with only amphibians in 
#excludes the single species orthologs 
#inputs: directory of GO***.fa sequences from orthofinder results and Orthogroups.GeneCount.tsv

import os
from Bio import SeqIO
import csv
###Finds orthologs which are unique to amphibians excluding single species orthologs

#######WORKS - it is a combination of both the amphi4.py and the excelgenecounts2.py to 
###exlude species specfic orthogroups and makes it unqiue for amphibians


# Specify the path to the TSV file from orthofinder output Orthogroups.GeneCount.tsv
tsv_file = '/gpfs01/home/mbxrs14/orthofinder_names_protein_ple/OrthoFinder/Results_Jun13_1/Orthogroups/Orthogroups.GeneCount.tsv'

# Read the TSV file
with open(tsv_file, 'r') as file:
    reader = csv.reader(file, delimiter='\t')
    header = next(reader)  # Read the header row

# Find orthogroups where any species has the same gene count as the total column ro get rid of single species orthologs 
    orthogroups = []
    for row in reader:
        orthogroup = row[0]
        gene_counts = [int(count) for count in row[1:-1]]  # Convert gene counts to integers
        total_count = int(row[-1])  # Total gene count

        # Check if any species has the same gene count as the total column
        if any(count == total_count for count in gene_counts):
            orthogroups.append(orthogroup)

##path containing the OG0000** files you want to filter through 
folder_path = '/gpfs01/home/mbxrs14/orthofinder_names_protein_ple/OrthoFinder/Results_Jun13_1/Orthogroup_Sequences'

# Excluded organisms
excluded_organisms = ['Alligatormississippiensis', 'Apusapus', 'Aquilachrysaetos',
                      'Balaenopteramusculus', 'Ceratotheriumsimum', 'Choloepusdidactylus',
                      'Columbalivia', 'Desmodusrotundus', 'Dromaiusnovaehollandiae', 'Elephasmaximum',
                      'Eublepharismacularius', 'Ornithorhynchusanatinus', 'Gopherusevgoodei', 'Gorillagorilla',
                      'Nipponianippon', 'Numidameleagris', 'Sarcophilusharrisi', 'Sphenodonpunctatus', 'Susscrofa',
                      'Taeniopygiaguttata', 'Tupaiachinensis', 'Varanuskomodoensis', 'cuculuscanorus']



# Get the list of .fa files in the directory
fa_files = [file for file in os.listdir(folder_path) if file.endswith('.fa')]

# Get the list of .fa files in the directory
fa_files = [file for file in os.listdir(folder_path) if file.endswith('.fa')]

# Initialize a counter for files not containing excluded organisms or orthologs
num_valid_files = 0


# Open the output file for writing
output_file = open('/gpfs01/home/mbxrs14/orthofinder_names_protein_ple/OrthoFinder/Results_Jun13_1/amphibianspecific_output.txt', 'w')


# Iterate through each .fa file
for fa_file in fa_files:
    file_path = os.path.join(folder_path, fa_file)
    organism_names = set()  # To store unique organism names within each file
    
    # Parse the FASTA file and extract organism names from each sequence
    with open(file_path, 'r', encoding='utf-8') as fasta_file:
        records = list(SeqIO.parse(fasta_file, 'fasta'))
        
        # Skip files with only one sequence
        if len(records) <= 1:
            continue
        
        for record in records:
            header = record.description
            organism_name = header.strip().lstrip('>').split('_')[0]
            organism_names.add(organism_name)
    
    # Check if any excluded organism is present in the file
    contains_excluded_organisms = any(org in excluded_organisms for org in organism_names)


    # Check if any excluded ortholog is present in the file
    contains_excluded_orthologs = any(ortho in fa_file for ortho in orthogroups)
    
    # Print the name of the file and the genes if it does not contain excluded organisms or orthologs
    if not contains_excluded_organisms and not contains_excluded_orthologs:
        num_valid_files += 1
        print(f"File {fa_file} does not contain excluded organisms or single-species orthologs.")
        output_file.write(f"File {fa_file} does not contain excluded organisms or orthologs.\n")
        output_file.write(str(num_valid_files) + '\n')

# Close the output file
output_file.close()

# Print the number of valid files
print(f"Number of valid files: {num_valid_files}")

