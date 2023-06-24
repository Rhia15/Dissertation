#This file filters the base_change.tab file to only include the orthogroups which have been significantly expanded or contracted 
#use before expansionscontractions.py 
#significance text file created through CAFE5 github instructions 
#Also converted the base_change.tab to base_change.tsv file 
#output also tells you which families were removed 

import csv

# Read significance file and extract the relevant family IDs
with open('/Users/rhianah/Documents/Dissertation/global_lambda_filtered_results/significant_0.05.txt', 'r') as file:
    lines = file.readlines()
    header = lines[0].strip().split('\t')
    family_ids = [line.split('\t')[0] for line in lines[1:]]

# Read the second file and keep rows with matching family IDs
output_rows = []
removed_family_ids = []
with open('/Users/rhianah/Documents/Dissertation/global_lambda_filtered_results/Base_change.tsv', 'r') as file:
    reader = csv.reader(file, delimiter='\t')
    header_row = next(reader)  # Store the header row

    for row in reader:
        if row[0] in family_ids:
            output_rows.append(row)
        else:
            removed_family_ids.append(row[0])

# Write the filtered rows to a new file - input the path to the new tsv file 
with open('/Users/rhianah/Documents/Dissertation/global_lambda_filtered_results/output0.05_file.tsv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='\t')
    writer.writerow(header_row)  # Write the header row
    writer.writerows(output_rows)
print("Removed Family IDs:")
for family_id in removed_family_ids:
    print(family_id)


