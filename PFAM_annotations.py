def create_dictionary_from_file(file_path):
    data_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('#') or line.startswith('##'):
                continue  # Skip comment lines or lines starting with #
            line = line.strip()  # Remove leading/trailing whitespaces
            gene_name, pfam_info = line.split(' ', 1)  # Split the line based on the first space character
            data_dict[gene_name] = pfam_info
    return data_dict

def find_matching_values(keys_file_path, data_dict, output_file_path):
    matching_values = {}
    with open(keys_file_path, 'r') as keys_file:
        for key in keys_file:
            key = key.strip()  # Remove leading/trailing whitespaces
            matching_value = data_dict.get(key)
            if matching_value is not None:
                matching_values[key] = matching_value
    
    with open(output_file_path, 'w') as output_file:
        for key, value in matching_values.items():
            output_file.write(f"{key}\t{value}\n")

# File path to dictionary (col 1 = header_, (cold 2 = PFAM) 
data_file_path = '/gpfs01/home/mbxrs14/motif_mapping2/new_file.txt'

# File path containing the list of keys (gene names)
keys_file_path = '/gpfs01/home/mbxrs14/motif_mapping2/OG0001255_amphibians_headers.txt'

# File path to save the output
output_file_path = '/gpfs01/home/mbxrs14/motif_mapping2/OG0001255_amphibians_headers_output.txt'

# Create the dictionary from the data file
result_dict = create_dictionary_from_file(data_file_path)

# Find the matching values for the keys provided in the keys file and save to the output file
find_matching_values(keys_file_path, result_dict, output_file_path)
