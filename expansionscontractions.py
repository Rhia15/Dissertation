#This file takes the output of filtercaferesults.py and 
#uses it to provide a text file containing the number of contractions and expansions at eahc node
#A list of which orthologs were contracted or expanded at each node 

import csv

def write_changed_ids_to_file(file_path, output_file):
    with open(file_path, 'r', newline='') as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        headers = next(reader)  # Read the header row

        changed_ids = {}
        for header_index, header_name in enumerate(headers[1:], start=1):
            increased_ids = []
            decreased_ids = []
            for row in reader:
                try:
                    value = int(row[header_index])
                    if value > 0:
                        increased_ids.append(row[0])
                    elif value < 0:
                        decreased_ids.append(row[0])
                except (ValueError, IndexError):
                    pass

            changed_ids[header_name] = {"increased_ids": increased_ids, "decreased_ids": decreased_ids}
            tsvfile.seek(0)  # Reset the file pointer for each header

    with open(output_file, 'w') as outfile:
        for header_name, ids in changed_ids.items():
            increased_ids = ids["increased_ids"]
            decreased_ids = ids["decreased_ids"]
            outfile.write(f"Header: {header_name}\n")
            outfile.write(f"Number of Family IDs with increased values: {len(increased_ids)}\n")
            outfile.write("List of Family IDs with increased values:\n")
            for family_id in increased_ids:
                outfile.write(family_id + '\n')
            outfile.write(f"Number of Family IDs with decreased values: {len(decreased_ids)}\n")
            outfile.write("List of Family IDs with decreased values:\n")
            for family_id in decreased_ids:
                outfile.write(family_id + '\n')
            outfile.write('\n')

# Example usage
file_path = '/Users/rhianah/Documents/Dissertation/global_lambda_filtered_results/output0.05_file.tsv'
output_file = '/Users/rhianah/Documents/Dissertation/Changed_IDs0.05.txt'
write_changed_ids_to_file(file_path, output_file)
