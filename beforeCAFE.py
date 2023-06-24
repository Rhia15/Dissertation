#This input for this script is the Orthogroups.GeneCount.tsv file from orthofinder 
#Outputs a tsv for the cafe analysis 

#removes single species orthogroups by removing species with gene counts matching the toal 
#removes gene families with gene counts greater than 100 to account for large size differentials
#Provides a list of the gene families removed 


import csv

# Define the input and output file paths
input_file = '/Users/rhianah/Documents/Dissertation/orthofinder_names_protein_ple/Orthogroups.GeneCount.tsv'
output_file = '/Users/rhianah/Documents/Dissertation/orthofinder_names_protein_ple/genecount_edited.tsv'


#save the stats into a text file 
# Define the statistics file path
stats_file = output_file.replace('.tsv', '_stats.txt')



# Open the input file
with open(input_file, 'r') as f_in:
    reader = csv.reader(f_in, delimiter='\t')
    header = next(reader)  # Read the header row
    rows_to_keep = []
    removed_orthogroups_counts = {
        'matching_counts': 0,
        'counts_gt_100': 0
    }
    total_gene_count = 0
    removed_gene_count = 0

    # Iterate over each row in the file
    for row in reader:
        orthogroup = row[0]
        total_count = int(row[-1])
        species_counts = [int(count) for count in row[1:-1]]  # Convert counts to integers

        # Check if any species count matches the total count or exceeds 100
        if any(count == total_count for count in species_counts):
            removed_orthogroups_counts['matching_counts'] += 1
        elif any(count > 100 for count in species_counts):
            removed_orthogroups_counts['counts_gt_100'] += 1
            removed_gene_count += total_count
        else:
            rows_to_keep.append(row)  # Keep this row
            total_gene_count += total_count

    # Write the filtered rows to the output file
    with open(output_file, 'w', newline='') as f_out:
        writer = csv.writer(f_out, delimiter='\t')
        writer.writerow(header)
        for row in rows_to_keep:
            writer.writerow(row)


# Save the statistics to the text file
with open(stats_file, 'w') as f_stats:
    
    f_stats.write("Number of orthogroups removed (matching counts): {}\n".format(removed_orthogroups_counts['matching_counts']))
    f_stats.write("Number of orthogroups removed (counts > 100): {}\n".format(removed_orthogroups_counts['counts_gt_100']))
    f_stats.write("Number of orthogroups in the final output: {}\n".format(len(rows_to_keep)))
    f_stats.write("Total gene count in the final output: {}\n".format(total_gene_count))
    f_stats.write("Number of genes removed: {}\n".format(removed_gene_count))

print("Rows with matching gene counts or counts >100 removed. Output saved to", output_file)
print("Number of orthogroups removed (matching counts):", removed_orthogroups_counts['matching_counts'])
print("Number of orthogroups removed (counts > 100):", removed_orthogroups_counts['counts_gt_100'])
print("Total gene count in the final output:", total_gene_count)
print("Number of orthogroups in the final output:", len(rows_to_keep))
print("Number of genes removed:", removed_gene_count)
